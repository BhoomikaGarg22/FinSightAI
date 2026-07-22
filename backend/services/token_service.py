"""
Token Service

Handles secure token generation.
"""

import secrets
from datetime import datetime, timedelta


TOKEN_EXPIRY_HOURS = 24


def generate_verification_token():
    """
    Returns:
        token, expiry_datetime
    """

    token = secrets.token_urlsafe(32)

    expires = datetime.utcnow() + timedelta(
        hours=TOKEN_EXPIRY_HOURS
    )

    return token, expires


def generate_reset_token():
    """
    Returns:
        token, expiry_datetime
    """

    token = secrets.token_urlsafe(32)

    expires = datetime.utcnow() + timedelta(
        hours=1
    )

    return token, expires