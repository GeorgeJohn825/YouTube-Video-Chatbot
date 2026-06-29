from pydantic import BaseModel, HttpUrl, Field
from typing import Optional

class CreateVideoSchema(BaseModel):
    youtube_url: HttpUrl = Field(..., description="YouTube video URL")
    title: Optional[str] = None
    thumbnail: Optional[HttpUrl] = None
    transcript: Optional[str] = None

class VideoResponseSchema(BaseModel):
    id: int
    youtube_url: HttpUrl
    title: str
    thumbnail: Optional[HttpUrl]
    created_at: str

    class Config:
        orm_mode = True
