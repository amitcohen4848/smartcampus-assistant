import sqlite3
import logging
from config import DB_PATH

# Let me log and follow conection to DB
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_connection():
    try:
        conn = sqlite3.connect(DB_PATH)

        # convert it to dictionary
        conn.row_factory = sqlite3.Row

        conn.execute("PRAGMA foreign_keys = ON")
        logger.info("Database Connection Successfully")
        return conn

    except sqlite3.Error as e:
        logger.error(f"Database connection failed: {e}")
        raise