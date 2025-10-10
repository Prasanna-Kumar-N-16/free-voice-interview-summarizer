from __future__ import annotations
from typing import Optional
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.pool import StaticPool

# Simple SQLite wrapper; creates tables if missing

def get_engine(db_url: str = "sqlite+pysqlite:///./data.db") -> Engine:
    # Use StaticPool to avoid multiple connections in uvicorn reload mode
    engine = create_engine(
        db_url,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    with engine.begin() as conn:
        conn.execute(text(
            """
            CREATE TABLE IF NOT EXISTS transcripts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT,
                transcript TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
            """
        ))
    return engine