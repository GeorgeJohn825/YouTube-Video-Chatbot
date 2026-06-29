import os
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from backend.database import engine, Base
from backend.routers import auth, users, videos, chat

app = FastAPI(title="YouTube Learning Assistant",
              description="FastAPI backend with RAG for YouTube videos",
              version="0.1.0")

# Allow all origins for simplicity; adjust in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(videos.router, prefix="/videos", tags=["videos"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])

# Create tables on startup
@app.on_event("startup")
async def startup_event():
    async def create_tables():
        # Synchronous call is fine for SQLite
        Base.metadata.create_all(bind=engine)
    create_tables()

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "YouTube Learning Assistant API is running"}
