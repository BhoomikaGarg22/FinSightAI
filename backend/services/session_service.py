import hashlib
import secrets
from datetime import datetime, timedelta, timezone

from backend.db import get_connection


SESSION_DURATION_DAYS = 7


def create_session(user_id):
    # Generate a random token for the browser
    token = secrets.token_urlsafe(32)

    # Store only the token's hash in the database
    token_hash = hashlib.sha256(token.encode()).hexdigest()

    expires_at = (
        datetime.now(timezone.utc) + timedelta(days=SESSION_DURATION_DAYS)
    ).isoformat()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO user_sessions (user_id, token_hash, expires_at)
        VALUES (?, ?, ?)
        """,
        (user_id, token_hash, expires_at),
    )

    conn.commit()
    conn.close()

    # Return the raw token to be placed in the browser cookie
    return token


def get_session_user_id(token):
    if not token:
        return None

    token_hash = hashlib.sha256(token.encode()).hexdigest()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT user_id, expires_at
        FROM user_sessions
        WHERE token_hash = ?
        """,
        (token_hash,),
    )

    session = cursor.fetchone()
    conn.close()

    if not session:
        return None

    expires_at = datetime.fromisoformat(session["expires_at"])

    if expires_at <= datetime.now(timezone.utc):
        delete_session(token)
        return None

    return session["user_id"]


def delete_session(token):
    if not token:
        return

    token_hash = hashlib.sha256(token.encode()).hexdigest()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM user_sessions WHERE token_hash = ?",
        (token_hash,),
    )

    conn.commit()
    conn.close()
