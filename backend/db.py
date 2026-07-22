import sqlite3
from pathlib import Path

# FinSightAI project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Database folder
DB_DIR = BASE_DIR / "database"

# Create database folder if it doesn't exist
DB_DIR.mkdir(exist_ok=True)

# Database file
DB_PATH = DB_DIR / "database.db"


def get_connection():
    """Return SQLite connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn