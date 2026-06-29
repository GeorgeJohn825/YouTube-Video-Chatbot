from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from pathlib import Path

# SQLite database path inside the workspace
BASE_DIR = Path(__file__).resolve().parent.parent
SQLITE_PATH = BASE_DIR / "app.db"

engine = create_engine(f"sqlite:///" + str(SQLITE_PATH), connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency for FastAPI endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
