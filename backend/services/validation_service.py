"""
Validation Service

Contains reusable validation helpers for:

- Name
- Email
- Password
"""

import re

from email_validator import (
    validate_email as email_validate,
    EmailNotValidError,
)


# =====================================================
# Name Validation
# =====================================================

def validate_name(name: str):

    if not name.strip():
        return False, "Name is required."

    return True, None


# =====================================================
# Email Validation
# =====================================================

def validate_email(email: str):

    try:

        email_validate(
            email,
            check_deliverability=False,
        )

    except EmailNotValidError:

        return False, "Enter a valid email address."

    return True, None

# =====================================================
# Password Validation
# =====================================================

def validate_password(password: str):

    if len(password) < 8:
        return False, "Password must be at least 8 characters."

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."

    if not re.search(r"\d", password):
        return False, "Password must contain at least one number."

    return True, None