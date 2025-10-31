"""Module for handling the SQLite database connection and caching."""
import sqlite3
import json
import logging
from typing import Optional, Dict, Any
from pathlib import Path

# Define the database path relative to the project's data directory
DB_FILE = Path(__file__).parent.parent.parent / "data" / "name_cache.db"
DB_FILE.parent.mkdir(parents=True, exist_ok=True)

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def setup_database():
    """Sets up the database table if it doesn't exist."""
    conn = get_db_connection()
    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS names (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                data TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        logging.info("Database table 'names' is set up.")
    except sqlite3.Error as e:
        logging.error(f"Database setup failed: {e}")
    finally:
        conn.close()

def get_cached_name(name: str) -> Optional[Dict[str, Any]]:
    """
    Retrieves cached data for a given name.

    Args:
        name: The name to look up in the cache.

    Returns:
        The cached data as a dictionary, or None if not found.
    """
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT data FROM names WHERE name = ?", (name,))
        row = cursor.fetchone()
        if row:
            logging.info(f"Found cached data for '{name}'.")
            return json.loads(row['data'])
        return None
    finally:
        conn.close()

def cache_name(name: str, data: Dict[str, Any]):
    """
    Caches the data for a given name.

    Args:
        name: The name to cache.
        data: The data dictionary to cache.
    """
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO names (name, data) VALUES (?, ?)",
            (name, json.dumps(data))
        )
        conn.commit()
        logging.info(f"Cached data for '{name}'.")
    except sqlite3.Error as e:
        logging.error(f"Failed to cache data for '{name}': {e}")
    finally:
        conn.close()

# Initialize the database when this module is loaded
setup_database()
