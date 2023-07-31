from __future__ import unicode_literals
import os
import logging
import configparser
import argparse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.database_operations import get_database_engine
from database.database_operations import initialize_database
from database.database_operations import create_video_record
from database.database_operations import create_download_record
from database.database_operations import create_lbry_upload_record
from database.database_operations import update_lbry_upload_record
from downloader.youtube import YouTubeProcessor
from uploader.lbry import LBRYUploader


# Set up logging
logging.basicConfig(
        filename='app.log', 
        level=logging.ERROR, 
        format='%(asctime)s - %(levelname)s - %(message)s'
)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process a YouTube video and upload it to LBRY.')
    parser.add_argument('youtube_url', type=str, help='URL of the YouTube video to process and upload to LBRY.')
    return parser.parse_args()

def read_config(config_file):
    """
    Read and parse the configuration file.

    Args:
        config_file (str): Path to the configuration file.

    Returns:
        configparser.ConfigParser: The parsed configuration object.
    """
    config = configparser.ConfigParser()
    config.read(config_file)

    return config

def main():
    # Read the configuration file
    config = read_config('config.ini')
    download_archive = config.get('Downloader', 'download_archive')
    download_archive_dir = os.path.abspath(
            config.get('Downloader', 'download_archive_dir')
    )

    # Read settings from the configuration file
    channel_id = config.get('LBRY', 'channel_id')
    ydl_opts = {
        'simulate': config.getboolean('Downloader', 'simulate'),
        'download_archive': os.path.join(download_archive_dir, download_archive),
        'format': config.get('Downloader', 'format'),
        'outtmpl': config.get('Downloader', 'outtmpl'),

    }

    args = parse_arguments()
    url = args.youtube_url

    try:
        # Video processing
        youtube_processor = YouTubeProcessor(download_archive_dir, url, ydl_opts)
        video_info = youtube_processor.process_video()

        # Database operations
        engine = get_database_engine(config)
        Session = sessionmaker(bind=engine)

        with Session() as session:
            # Create tables if they don't exist
            initialize_database(engine)

            # Perform database operations within a transaction block
            session.begin()

            create_video_record(session, video_info, url)
            create_download_record(session, video_info)
            create_lbry_upload_record(session, video_info)

            session.commit()

            # LBRY upload
            lbry_uploader = LBRYUploader()
            lbry_url = lbry_uploader.upload(video_info)

            # Update LBRYUpload record with the LBRY URL and status
            if lbry_url:
                print(f"LBRY URL: {lbry_url}")

                # Set status to success
                update_lbry_upload_record(
                        session, 
                        video_info['id'], 
                        lbry_url, 
                        lbry_status=1
                )

                session.commit()
            else:
                print("LBRY upload failed.")

                # Set status to failed
                update_lbry_upload_record(
                        session, 
                        video_info['id'], 
                        lbry_url=None, 
                        lbry_status=-1
                )

                session.commit()
    
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occured: {e}")

if __name__ == "__main__":
    main()
