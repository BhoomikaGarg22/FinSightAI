from datetime import datetime

from backend.db import get_connection
from backend.auth.hash import hash_password

from backend.services.token_service import (
    generate_reset_token,
)

from backend.services.email_service import (
    send_reset_password_email,
)

from backend.services.validation_service import (
    validate_password,
)


# =====================================================
# Send Password Reset Email
# =====================================================

def request_password_reset(email: str):

    email = email.strip().lower()

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            SELECT *

            FROM users

            WHERE email = ?
            """,
            (email,),
        )

        user = cursor.fetchone()

        if user is None:

            return (
                False,
                "No account exists with this email.",
            )

        token, expiry = generate_reset_token()

        cursor.execute(
            """
            UPDATE users

            SET

                reset_token = ?,
                reset_token_expires = ?

            WHERE id = ?
            """,
            (
                token,
                expiry.isoformat(),
                user["id"],
            ),
        )

        conn.commit()

    finally:

        conn.close()

    success, message = send_reset_password_email(
        email,
        token,
    )

    if not success:

        return False, message

    return (
        True,
        "Password reset email sent successfully.",
    )


# =====================================================
# Reset Password
# =====================================================

def reset_password(
    token: str,
    new_password: str,
):

    # -------------------------------
    # Validate Password
    # -------------------------------

    valid, error = validate_password(
        new_password,
    )

    if not valid:

        return (
            False,
            error,
        )

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            SELECT *

            FROM users

            WHERE reset_token = ?
            """,
            (token,),
        )

        user = cursor.fetchone()

        if user is None:

            return (
                False,
                "Invalid password reset link.",
            )

        expires = user["reset_token_expires"]

        if expires:

            try:

                expiry = datetime.fromisoformat(
                    expires
                )

            except ValueError:

                return (
                    False,
                    "Invalid password reset token.",
                )

            if datetime.utcnow() > expiry:

                return (
                    False,
                    "Password reset link has expired.",
                )

        hashed_password = hash_password(
            new_password
        )

        cursor.execute(
            """
            UPDATE users

            SET

                password = ?,

                reset_token = NULL,

                reset_token_expires = NULL

            WHERE id = ?
            """,
            (
                hashed_password,
                user["id"],
            ),
        )

        conn.commit()

        return (
            True,
            "Password updated successfully.",
        )

    finally:

        conn.close()