from datetime import datetime

from backend.db import get_connection


# =====================================================
# Email Verification
# =====================================================

def verify_email(token: str):
    """
    Verify a user's email using the verification token.

    Returns:
        (bool, str)
    """

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            SELECT *

            FROM users

            WHERE verification_token = ?
            """,
            (token,),
        )

        user = cursor.fetchone()

        if user is None:

            return (
                False,
                "Invalid verification link.",
            )

        if user["is_verified"]:

            return (
                False,
                "This account has already been verified.",
            )

        expires = user["verification_token_expires"]

        if expires:

            try:

                expiry = datetime.fromisoformat(expires)

            except ValueError:

                return (
                    False,
                    "Verification token is corrupted.",
                )

            if datetime.utcnow() > expiry:

                return (
                    False,
                    "This verification link has expired.",
                )

        cursor.execute(
            """
            UPDATE users

            SET

                is_verified = 1,

                verification_token = NULL,

                verification_token_expires = NULL

            WHERE id = ?
            """,
            (
                user["id"],
            ),
        )

        conn.commit()

        return (
            True,
            "Your email has been verified successfully.",
        )

    finally:

        conn.close()


# =====================================================
# Check Verification Status
# =====================================================

def is_email_verified(email: str):
    """
    Returns True if the user's email is verified.
    """

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            SELECT is_verified

            FROM users

            WHERE email = ?
            """,
            (
                email.lower().strip(),
            ),
        )

        user = cursor.fetchone()

        if user is None:
            return False

        return bool(user["is_verified"])

    finally:

        conn.close()