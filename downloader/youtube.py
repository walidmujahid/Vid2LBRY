from __future__ import unicode_literals
import os
import re
import subprocess

from youtube_dl import YoutubeDL


class YouTubeProcessor:
    def __init__(self, download_archive, youtube_url, ydl_opts):
        """
        Initialize the YouTubeProcessor.

        Args:
            download_archive (str): Path to the download archive directory.
            youtube_url (str): The URL of the YouTube video to process.
            ydl_opts (dict): Options for youtube-dl.
        """
        self.download_archive = download_archive
        self.video_source = 'youtube'
        self.youtube_url = youtube_url
        self.ydl_opts = ydl_opts

    def is_valid_youtube_url(self):
        """
        Check if the provided URL is a valid YouTube URL.

        Returns:
            bool: True if the URL is valid, False otherwise.
        """
        pattern = r'^(https?\:\/\/)?(www\.)?(youtube\.com|youtu\.?be)\/.+$'
        return bool(re.match(pattern, self.youtube_url))

    def process_video(self):
        """
        Process the YouTube video by downloading and post-processing.

        Returns:
            dict: The video information dictionary.
        """
        if not self.is_valid_youtube_url():
            raise ValueError("Invalid YouTube URL: Please provide a valid YouTube URL.")

        with YoutubeDL(self.ydl_opts) as ydl:
            video_info = ydl.extract_info(
                    self.youtube_url, download=True
        )

        video_info['video_source'] = self.video_source

        # Check if the downloaded file is already in MP4 format
        mp4_filename = os.path.join(
                self.download_archive, 
                f"{video_info['id']}.mp4"
        )

        if os.path.exists(mp4_filename):
            # Set the downloaded file path to the MP4 file directly
            video_info['download_path'] = mp4_filename

        else:
            # Perform post-processing using ffmpeg to convert to MP4 format
            original_filename = os.path.join(
                    self.download_archive, 
                    f"{video_info['id']}.{video_info['ext']}"
            )
            mp4_filename = os.path.join(
                    self.download_archive, 
                    f"{video_info['id']}.mp4"
            )
            subprocess.run(
                    [
                        'ffmpeg', 
                        '-i', 
                        original_filename, 
                        '-c', 
                        'copy', 
                        mp4_filename
                    ], 

                    check=True
            )

            # Set the downloaded file path to the MP4 file
            video_info['download_path'] = mp4_filename

        return video_info

