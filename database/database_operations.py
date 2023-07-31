from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import Base
from database.models import Video
from database.models import Download
from database.models import LBRYUpload


Session = sessionmaker()

def get_database_engine(config):
    """
    Get the database engine based on the configuration.

    Args:
        config (ConfigParser): The configuration object.

    Returns:
        sqlalchemy.engine.Engine: The SQLAlchemy database engine.
    """
    db_type = config.get('Database', 'dialect')
    if db_type == 'sqlite':
        db_path = config.get('sqlite', 'db_path')
        engine = create_engine(f'sqlite:///{db_path}', echo=True)
    elif db_type == 'mysql':
        # untested
        db_host = config.get('mysql', 'host')
        db_port = config.getint('mysql', 'port')
        db_user = config.get('mysql', 'user')
        db_password = config.get('mysql', 'password')
        db_name = config.get('mysql', 'name')
        engine = create_engine(f'mysql:///{db_user}:{db_password}@{db_host}:{db_port}/{db_name}', echo=True)
    elif db_type == 'postgresql':
        # untested
        db_host = config.get('postgresql', 'host')
        db_port = config.getint('postgresql', 'port')
        db_user = config.get('postgresql', 'user')
        db_password = config.get('postgresql', 'password')
        db_name = config.get('postgresql', 'name')
        engine = create_engine(f'postgresql:///{db_user}:{db_password}@{db_host}:{db_port}/{db_name}', echo=True)
    else:
        raise ValueError(f"Invalid database type: {db_type}")

    return engine

def initialize_database(engine):
    """
    Create all database tables if they don't exist.

    Args:
        engine (sqlalchemy.engine.Engine): The SQLAlchemy database engine.
    """
    Session.configure(bind=engine)
    Base.metadata.create_all(engine)

def create_video_record(
        session, 
        video_info: dict,
        video_url: str
    ):
    """
    Create a new Video record in the database.

    Args:
        session (sqlalchemy.orm.Session): The SQLAlchemy database session.
        video_info (dict): The video information dictionary.
        youtube_url (str): The URL of the YouTube video.
    """
    try:
        video = Video(
            video_source=video_info['video_source'],
            video_id=video_info['id'],
            title=video_info['title'],
            description=video_info['description'],
            video_url=video_url,
            thumbnail_url=video_info['thumbnail']
        )
        session.merge(video)
    except Exception as e:
        session.rollback()
        raise e

def create_download_record(session, video_info: dict):
    """
    Create a new Download record in the database.

    Args:
        session (sqlalchemy.orm.Session): The SQLAlchemy database session.
        video_info (dict): The video information dictionary.
    """
    try:
        download = Download(
            video_source=video_info['video_source'],
            video_id=video_info['id'], 
            download_path=video_info['download_path']
        )
        session.add(download)
    except Exception as e:
        session.rollback()
        raise e

def create_lbry_upload_record(session, video_info: dict):
    """
    Create a new LBRYUpload record in the database.

    Args:
        session (sqlalchemy.orm.Session): The SQLAlchemy database session.
        video_info (dict): The video information dictionary.
    """
    try:
        lbry_upload = LBRYUpload(
            video_source=video_info['video_source'],
            video_id=video_info['id'],
            lbry_status=0, 
            lbry_url=None
        )
        session.add(lbry_upload)
    except Exception as e:
        session.rollback()
        raise e

def update_lbry_upload_record(
        session, 
        video_id: str,
        lbry_url: str, 
        lbry_status: int
    ):
    """
    Update the LBRYUpload record in the database.

    Args:
        session (sqlalchemy.orm.Session): The SQLAlchemy database session.
        video_id (str): The ID of the video.
        lbry_url (str): The LBRY URL of the uploaded video.
        lbry_status (int): The status of the LBRY upload (-1: Failed, 0: Pending, 1: Success).
    """
    try:
        lbry_upload = session.query(LBRYUpload).filter(LBRYUpload.video_id == video_id).one()
        lbry_upload.lbry_url = lbry_url
        lbry_upload.lbry_status = lbry_status
    except Exception as e:
        session.rollback()
        raise e
