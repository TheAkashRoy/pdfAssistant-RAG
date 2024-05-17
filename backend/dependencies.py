from typing import Generator
import sqlite3
import contextlib

from fastapi import Depends, HTTPException, status
from pydantic import BaseModel

# Define a Pydantic model for the database connection
class DatabaseConnection(BaseModel):
    connection: sqlite3.Connection
    class Config:
        arbitrary_types_allowed = True

# Define a function to create a database connection
@contextlib.contextmanager
def get_db_connection() -> Generator[DatabaseConnection, None, None]:
    try:
        connection = sqlite3.connect("database.db")
        yield DatabaseConnection(connection=connection)
    finally:
        connection.close()

# Define a function to handle database errors
def handle_database_error(func):
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except sqlite3.Error as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Database error: {e}",
            )
    return wrapper

# Use the database connection as a dependency
def get_db() -> DatabaseConnection:
    return Depends(get_db_connection)

# id INTEGER PRIMARY KEY,
# Filename TEXT,
# Created_at DATETIME
