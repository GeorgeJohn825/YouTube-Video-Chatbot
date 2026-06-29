from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.database import Base

class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    youtube_url = Column(String, unique=True, nullable=False, index=True)
    title = Column(String, nullable=False)
    thumbnail = Column(String, nullable=True)
    transcript = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    chats = relationship("ChatHistory", back_populates="video", cascade="all, delete-orphan")
