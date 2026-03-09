import sqlite3
import logging
from config import DB_PATH

# Let me log and follow connection to DB
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Ensure Connection to DB
def get_connection():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
    except sqlite3.Error as e:
        logger.error(f"Database connection failed: {e}")
        raise


# Dependency in DB, allow open connection and close it even if Crash.
def get_db():
    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()