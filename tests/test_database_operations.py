from configparser import ConfigParser
import pytest
import os
import sys

# Get the parent directory of the current directory (vid2lbry directory)
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the parent directory to the Python module search path
sys.path.insert(0, parent_dir)

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import Base
from database.models import Video
from database.models import Download
from database.models import LBRYUpload
from database.database_operations import get_database_engine
from database.database_operations import initialize_database
from database.database_operations import create_video_record
from database.database_operations import create_download_record
from database.database_operations import create_lbry_upload_record
from database.database_operations import update_lbry_upload_record


def load_test_config():
    config = ConfigParser()
    config.read("tests/test_config.ini")
    return config

@pytest.fixture(scope="function")
def db_session(request):
    db_type = request.config.getoption("--db-type")

    # Load the test configuration from the config file
    config = load_test_config()    

    engine = get_database_engine(config)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Initialize the database with tables
    Base.metadata.create_all(engine)

    return session


# Test cases for database operations

def test_create_video_record(db_session):
    # Test creating a video record in the database
    try:
        # Sample video information
        video_source = 'youtube'
        video_url = 'https://youtu.be/PXTsVwd_j5A'
        video_id = 'PXTsVwd_j5A'
        title = 'THE JAMIL AL-AMIN CONSPIRACY'
        description = 'The Jamil Al-Amin (H. Rap Brown) Conspiracy. A true leader who walked with Martin Luther King, propagated the ideas of Malcolm X and became the Minister of Defense of the Black Panther Party is still alive and jailed under suspicious circumstances. Free Jamil Al Amin!'
        video_url = 'https://www.youtube.com/watch?v=test_video_id'
        thumbnail_url = 'https://example.com/sample_thumbnail.jpg'
        video_info = {
            'video_source': 'youtube',
            'id': video_id,
            'title': title,
            'description': description,
            'thumbnail': thumbnail_url,
        }

        # Perform the operation
        create_video_record(db_session, video_info, video_url)

        # Check if the video record is created
        video = db_session.query(Video).filter(Video.video_id == video_id).first()
        assert video is not None, "Video record not found"
        assert video.video_source == video_source, f"Expected {video_source}, but got {video.video_source}"
        assert video.title == title, f"Expected {title}, but got {video.title}"
        assert video.description == description, f"Expected {description}, but got {video.description}"
        assert video.video_url == video_url, f"Expected {video_url}, but got {video.video_url}"
        assert video.thumbnail_url == thumbnail_url, f"Expected {thumbnail_url}, but got {video.thumbnail_url}"
    except Exception as e:
        raise e
    finally:
        db_session.rollback()

def test_create_download_record(db_session):
    # Test creating a download record in the database
    try:
        # Sample video information
        video_source = 'youtube'
        video_id = 'PXTsVwd_j5A'
        download_path = 'download_archive/PXTsVwd_j5A.mp4'
        video_info = {
            'video_source': video_source,
            'id': video_id,
            'download_path': download_path,
        }

        # Perform the operation
        create_download_record(db_session, video_info)

        # Check if the download record is created
        download = db_session.query(Download).filter(Download.video_id == video_id).first()
        assert download is not None, "Download record not found"
        assert download.video_source == video_source, f"Expected {video_source}, but got {download.video_source}"
        assert download.video_id == video_id, f"Expected {video_id}, but got {download.video_id}"
        assert download.download_path == download_path, f"Expected {download_path}, but got {download.download_path}"
    except Exception as e:
        raise e
    finally:
        db_session.rollback()

def test_create_lbry_upload_record(db_session):
    # Test creating an LBRYUpload record in the database
    try:
        # Sample video information
        video_source = 'youtube'
        video_id = 'PXTsVwd_j5A'
        lbry_status = 0
        lbry_url = None
        video_info = {
            'video_source': video_source,
            'id': video_id,
        }

        # Perform the operation
        create_lbry_upload_record(db_session, video_info)

        # Check if the LBRYUpload record is created
        lbry_upload = db_session.query(LBRYUpload).filter(LBRYUpload.video_id == video_id).first()
        assert lbry_upload is not None, "LBRYUpload record not found"
        assert lbry_upload.video_source == video_source, f"Expected {video_source}, but got {lbry_upload.video_source}"
        assert lbry_upload.video_id == video_id, f"Expected {video_id}, but got {lbry_upload.video_id}"
        # on initial creation LBRYUpload records status should be 0
        assert lbry_upload.lbry_status == lbry_status, f"Expected {lbry_status}, but got {lbry_uplaod.lbry_status}"
        assert type(lbry_upload.lbry_status) is int, f"Expected {lbry_upload.lbry_status} to be of type class int"
        # on initial creation LBRYUpload records lbry_url should be None
        assert lbry_upload.lbry_url is lbry_url, f"Expected {lbry_upload.lbry_url} to be None"
    except Exception as e:
        raise e
    finally:
        db_session.rollback()

def test_update_lbry_upload_record(db_session):
    try:
        # Setup: Create an initial LBRYUpload record
        video_info = {
            'video_source': 'youtube',
            'id': 'PXTsVwd_j5A',
        }
        create_lbry_upload_record(db_session, video_info)

        # Test updating an LBRYUpload record in the database
        video_id = 'PXTsVwd_j5A'
        lbry_url = 'https://lbry.tv/@your_channel/PXTsVwd_j5A'
        lbry_status = 1

        # Perform the operation
        update_lbry_upload_record(db_session, video_id, lbry_url, lbry_status)

        # Check if the LBRYUpload record is updated
        lbry_upload = db_session.query(LBRYUpload).filter(LBRYUpload.video_id == video_id).first()

        # Assertions
        assert lbry_upload is not None, "LBRYUpload record not found"
        assert lbry_upload.video_id == video_id, f"Expected video_id {video_id}, but got {lbry_upload.video_id}"
        assert lbry_upload.lbry_url == lbry_url, f"Expected lbry_url {lbry_url}, but got {lbry_upload.lbry_url}"
        assert lbry_upload.lbry_status == lbry_status, f"Expected lbry_status {lbry_status}, but got {lbry_upload.lbry_status}"
        assert lbry_upload.video_source == 'youtube', f"Expected video_source 'youtube', but got {lbry_upload.video_source}"
        assert type(lbry_upload.lbry_status) is int, f"Expected {lbry_upload.lbry_status} to be of type class int"

        # Teardown: Delete the LBRYUpload record
        db_session.delete(lbry_upload)
        db_session.commit()
    except Exception as e:
        raise e
    finally:
        db_session.rollback()

# Error Scenarios
def test_update_nonexistent_lbry_upload_record(db_session):
    try:
        # Try updating a non-existent LBRYUpload record
        video_id = 'NON_EXISTENT_ID'
        lbry_url = 'https://lbry.tv/@your_channel/NON_EXISTENT_ID'
        lbry_status = 1

        # Expect an exception to be raised
        with pytest.raises(sqlalchemy.exc.NoResultFound):
            update_lbry_upload_record(db_session, video_id, lbry_url, lbry_status)
    except Exception as e:
        raise e
    finally:
        db_session.rollback()

