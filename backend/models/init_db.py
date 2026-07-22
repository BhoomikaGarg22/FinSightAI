from backend.db import get_connection, DB_PATH


# ==================================================
# Database Migration Helpers
# ==================================================

USER_PROFILE_COLUMNS = {
    "phone": "TEXT",
    "country": "TEXT DEFAULT 'India'",
    "occupation": "TEXT DEFAULT 'Student'",

    "investor_type": "TEXT DEFAULT 'Investor'",
    "risk_appetite": "TEXT DEFAULT 'Moderate'",
    "investment_experience": "TEXT DEFAULT 'Beginner'",
    "investment_horizon": "TEXT DEFAULT 'Long Term'",

    "investment_goals": "TEXT",
    "markets": "TEXT",

    "ai_style": "TEXT DEFAULT 'Balanced'",
    "response_length": "TEXT DEFAULT 'Medium'",
    "preferred_region": "TEXT DEFAULT 'Global'",
    "default_dashboard": "TEXT DEFAULT 'Overview'",

    "theme": "TEXT DEFAULT 'System'",
    "accent_color": "TEXT DEFAULT 'Blue'",
    "compact_dashboard": "INTEGER DEFAULT 0",
    "animations": "INTEGER DEFAULT 1",

    "language": "TEXT DEFAULT 'English'",
    "currency": "TEXT DEFAULT 'USD'",

    "notifications": "TEXT",

    "created_at": "TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
    "updated_at": "TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
}


def get_existing_columns(cursor, table_name):
    """
    Returns all existing columns for a table.
    """

    cursor.execute(f"PRAGMA table_info({table_name})")

    return {
        row["name"] if hasattr(row, "keys") else row[1]
        for row in cursor.fetchall()
    }


def migrate_user_profiles(cursor):
    """
    Automatically upgrades older databases without
    deleting any user data.

    Safe to run every startup.
    """

    existing_columns = get_existing_columns(
        cursor,
        "user_profiles",
    )

    for column, definition in USER_PROFILE_COLUMNS.items():

        if column not in existing_columns:

            print(f"➕ Adding column: {column}")

            cursor.execute(
                f"""
                ALTER TABLE user_profiles
                ADD COLUMN {column} {definition}
                """
            )

    print("✅ User profile schema is up-to-date.")

    # ==================================================
# Create Tables
# ==================================================

def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    # ==================================================
    # Users
    # ==================================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            email TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL,

            is_verified INTEGER DEFAULT 0,

            verification_token TEXT,

            verification_token_expires TIMESTAMP,

            reset_token TEXT,

            reset_token_expires TIMESTAMP,

            last_login TIMESTAMP,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # ==================================================
    # Chats
    # ==================================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chats(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER NOT NULL,

            question TEXT NOT NULL,

            answer TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(user_id)
            REFERENCES users(id)
            ON DELETE CASCADE
        )
    """)

    # ==================================================
    # Watchlist
    # ==================================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS watchlist(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER NOT NULL,

            symbol TEXT NOT NULL,

            company TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(user_id)
            REFERENCES users(id)
            ON DELETE CASCADE
        )
    """)

    # ==================================================
    # Uploaded Reports
    # ==================================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER NOT NULL,

            filename TEXT,

            filepath TEXT,

            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(user_id)
            REFERENCES users(id)
            ON DELETE CASCADE
        )
    """)

    # ==================================================
    # User Profiles
    # ==================================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_profiles(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER NOT NULL UNIQUE,

            phone TEXT,

            country TEXT DEFAULT 'India',

            occupation TEXT DEFAULT 'Student',

            investor_type TEXT DEFAULT 'Investor',

            risk_appetite TEXT DEFAULT 'Moderate',

            investment_experience TEXT DEFAULT 'Beginner',

            investment_horizon TEXT DEFAULT 'Long Term',

            investment_goals TEXT,

            markets TEXT,

            ai_style TEXT DEFAULT 'Balanced',

            response_length TEXT DEFAULT 'Medium',

            preferred_region TEXT DEFAULT 'Global',

            default_dashboard TEXT DEFAULT 'Overview',

            theme TEXT DEFAULT 'System',

            accent_color TEXT DEFAULT 'Blue',

            compact_dashboard INTEGER DEFAULT 0,

            animations INTEGER DEFAULT 1,

            language TEXT DEFAULT 'English',

            currency TEXT DEFAULT 'USD',

            notifications TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(user_id)
            REFERENCES users(id)
            ON DELETE CASCADE
        )
    """)

    # ==================================================
    # Automatic Schema Migration
    # ==================================================

    migrate_user_profiles(cursor)

    conn.commit()
    conn.close()

    print("=" * 60)
    print("✅ Database initialized successfully")
    print(f"📁 Location: {DB_PATH}")
    print("✅ User profile schema verified")
    print("=" * 60)


if __name__ == "__main__":
    create_tables()