from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class Video(Base):
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True)
    video_source = Column(String)
    video_id = Column(String, unique=True)
    title = Column(String)
    description = Column(String)
    video_url = Column(String)
    thumbnail_url = Column(String)
    downloads = relationship('Download', primaryjoin="Video.video_id==Download.video_id")
    uploads = relationship('LBRYUpload', primaryjoin="Video.video_id==LBRYUpload.video_id")

class Download(Base):
    __tablename__ = 'downloads'
    id = Column(Integer, primary_key=True)
    video_source = Column(String)
    video_id = Column(String, ForeignKey('videos.video_id'))
    download_path = Column(String)
    video = relationship(
        'Video',
        back_populates='downloads'
    )

class LBRYUpload(Base):
    __tablename__ = 'lbryuploads'
    id = Column(Integer, primary_key=True)
    video_source = Column(String)
    video_id = Column(String, ForeignKey('videos.video_id'))
    lbry_status = Column(Integer)
    lbry_url = Column(String)
    video = relationship(
        'Video', 
        back_populates='uploads'
    )


