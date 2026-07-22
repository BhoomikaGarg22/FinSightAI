import os
import json
import re

from backend.db import get_connection
from backend.auth.hash import hash_password, verify_password

from backend.services.token_service import (
    generate_verification_token,
)

from backend.services.email_service import (
    send_verification_email,
)

from backend.services.validation_service import (
    validate_name,
    validate_email,
    validate_password,
)

from backend.config.profile_defaults import (
    DEFAULT_PROFILE,
    JSON_FIELDS,
    get_default_profile,
)

# =====================================================
# Development Settings
# =====================================================

SKIP_EMAIL_VERIFICATION = (
    os.getenv("SKIP_EMAIL_VERIFICATION", "false").lower() == "true"
)

# =====================================================
# Registration Validation
# =====================================================

def validate_registration(
    name: str,
    email: str,
    password: str,
):

    valid, error = validate_name(name)

    if not valid:
        return False, error

    valid, error = validate_email(email)

    if not valid:
        return False, error

    valid, error = validate_password(password)

    if not valid:
        return False, error

    return True, None


# =====================================================
# Create Default User Profile
# =====================================================

def create_user_profile(user_id: int):

    profile = get_default_profile()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO user_profiles (

            user_id,

            phone,
            country,
            occupation,

            investor_type,
            risk_appetite,
            investment_experience,
            investment_horizon,

            investment_goals,
            markets,

            ai_style,
            response_length,
            preferred_region,
            default_dashboard,

            theme,
            accent_color,
            compact_dashboard,
            animations,

            language,
            currency,

            notifications

        )

        VALUES (

            ?, ?, ?, ?,

            ?, ?, ?, ?,

            ?, ?,

            ?, ?, ?, ?,

            ?, ?, ?, ?,

            ?, ?,

            ?

        )
        """,
        (
            user_id,

            profile["phone"],
            profile["country"],
            profile["occupation"],

            profile["investor_type"],
            profile["risk_appetite"],
            profile["investment_experience"],
            profile["investment_horizon"],

            json.dumps(profile["investment_goals"]),
            json.dumps(profile["markets"]),

            profile["ai_style"],
            profile["response_length"],
            profile["preferred_region"],
            profile["default_dashboard"],

            profile["theme"],
            profile["accent_color"],
            int(profile["compact_dashboard"]),
            int(profile["animations"]),

            profile["language"],
            profile["currency"],

            json.dumps(profile["notifications"]),
        ),
    )

    conn.commit()
    conn.close()


# =====================================================
# Get User Profile
# =====================================================

def get_user_profile(user_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM user_profiles
        WHERE user_id = ?
        """,
        (user_id,),
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return None

    profile = dict(row)

    # ---------------------------------------------
    # Decode JSON Fields
    # ---------------------------------------------

    defaults = get_default_profile()

    for field in JSON_FIELDS:

        value = profile.get(field)

        if not value:
            profile[field] = defaults[field]
            continue

        try:
            profile[field] = json.loads(value)

        except Exception:
            profile[field] = defaults[field]

    # ---------------------------------------------
    # Merge Missing Fields
    # ---------------------------------------------

    for key, value in defaults.items():

        if key not in profile:
            profile[key] = value

    return profile


# =====================================================
# Update User Profile
# =====================================================

def update_user_profile(user_id: int, settings: dict):

    """
    Save all profile settings.
    """

    profile = get_default_profile()
    profile.update(settings)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE user_profiles

        SET

            phone=?,
            country=?,
            occupation=?,

            investor_type=?,
            risk_appetite=?,
            investment_experience=?,
            investment_horizon=?,

            investment_goals=?,
            markets=?,

            ai_style=?,
            response_length=?,
            preferred_region=?,
            default_dashboard=?,

            theme=?,
            accent_color=?,
            compact_dashboard=?,
            animations=?,

            language=?,
            currency=?,

            notifications=?,

            updated_at=CURRENT_TIMESTAMP

        WHERE user_id=?
        """,
        (
            profile["phone"],
            profile["country"],
            profile["occupation"],

            profile["investor_type"],
            profile["risk_appetite"],
            profile["investment_experience"],
            profile["investment_horizon"],

            json.dumps(profile["investment_goals"]),
            json.dumps(profile["markets"]),

            profile["ai_style"],
            profile["response_length"],
            profile["preferred_region"],
            profile["default_dashboard"],

            profile["theme"],
            profile["accent_color"],
            int(profile["compact_dashboard"]),
            int(profile["animations"]),

            profile["language"],
            profile["currency"],

            json.dumps(profile["notifications"]),

            user_id,
        ),
    )

    conn.commit()
    conn.close()

    return True

    # =====================================================
# Create User
# =====================================================

def create_user(name: str, email: str, password: str):

    email = email.strip().lower()
    name = name.strip()

    print("=" * 60)
    print("Creating account for:", email)

    valid, error = validate_registration(
        name,
        email,
        password,
    )

    if not valid:
        print("Validation failed:", error)
        return False, error

    conn = get_connection()
    cursor = conn.cursor()

    # ---------------------------------------------
    # Check Existing User
    # ---------------------------------------------

    cursor.execute(
        """
        SELECT id
        FROM users
        WHERE email = ?
        """,
        (email,),
    )

    if cursor.fetchone():

        conn.close()

        print("Email already exists.")

        return (
            False,
            "An account with this email already exists.",
        )

    # ---------------------------------------------
    # Hash Password
    # ---------------------------------------------

    hashed_password = hash_password(password)

    verification_token, verification_expiry = (
        generate_verification_token()
    )

    print("Verification Token:", verification_token)

    # ---------------------------------------------
    # Create User
    # ---------------------------------------------

    cursor.execute(
        """
        INSERT INTO users (

            name,
            email,
            password,
            is_verified,
            verification_token,
            verification_token_expires

        )

        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            name,
            email,
            hashed_password,
            0,
            verification_token,
            verification_expiry.isoformat(),
        ),
    )

    # ---------------------------------------------
    # Create Default Profile
    # ---------------------------------------------

    user_id = cursor.lastrowid

    conn.commit()
    conn.close()

    create_user_profile(user_id)

    # ---------------------------------------------
    # Send Verification Email
    # ---------------------------------------------

    print("Calling send_verification_email()...")

    email_sent, message = send_verification_email(
        email,
        verification_token,
    )

    print("Email Sent:", email_sent)
    print("Email Service Message:", message)
    print("=" * 60)

    if not email_sent:

        return (
            False,
            f"Account created, but the verification email could not be sent.\n\n{message}",
        )

    return (
        True,
        "Account created successfully! Please check your inbox to verify your email.",
    )

    # =====================================================
# Login
# =====================================================

def login_user(email: str, password: str):

    email = email.strip().lower()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE email = ?
        """,
        (email,),
    )

    user = cursor.fetchone()

    # ---------------------------------------------
    # User Not Found
    # ---------------------------------------------

    if user is None:

        conn.close()

        return (
            False,
            "No account found with this email.",
        )

    # ---------------------------------------------
    # Verify Password
    # ---------------------------------------------

    if not verify_password(
        password,
        user["password"],
    ):

        conn.close()

        return (
            False,
            "Incorrect password.",
        )

    # ---------------------------------------------
    # Email Verification Check
    # ---------------------------------------------

    if (
        not user["is_verified"]
        and not SKIP_EMAIL_VERIFICATION
    ):

        conn.close()

        return (
            False,
            "Please verify your email before logging in.",
        )

    # ---------------------------------------------
    # Update Last Login
    # ---------------------------------------------

    cursor.execute(
        """
        UPDATE users

        SET last_login = CURRENT_TIMESTAMP

        WHERE id = ?
        """,
        (
            user["id"],
        ),
    )

    conn.commit()
    conn.close()

    user = dict(user)

# ---------------------------------------------
    # Load User Profile
    # ---------------------------------------------

    profile = get_user_profile(user["id"])

    if profile is None:

        # Existing account without profile
        create_user_profile(user["id"])
        profile = get_user_profile(user["id"])

    logged_in_user = {
        "id": user["id"],
        "username": user.get("username", ""),
        "email": user.get("email", ""),
        "created_at": user.get("created_at"),
        "is_verified": bool(user.get("is_verified", False)),
        "profile": profile,
    }

    return (
        True,
        logged_in_user,
    )
    # =====================================================
# Resend Verification Email
# =====================================================

def resend_verification_email(email: str):

    email = email.strip().lower()

    conn = get_connection()
    cursor = conn.cursor()

    # ---------------------------------------------
    # Find User
    # ---------------------------------------------

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

        conn.close()

        return (
            False,
            "No account found with this email.",
        )

    # ---------------------------------------------
    # Already Verified
    # ---------------------------------------------

    if user["is_verified"]:

        conn.close()

        return (
            False,
            "This account is already verified.",
        )

    # ---------------------------------------------
    # Generate New Verification Token
    # ---------------------------------------------

    verification_token, verification_expiry = (
        generate_verification_token()
    )

    cursor.execute(
        """
        UPDATE users

        SET

            verification_token = ?,
            verification_token_expires = ?

        WHERE id = ?
        """,
        (
            verification_token,
            verification_expiry.isoformat(),
            user["id"],
        ),
    )

    conn.commit()
    conn.close()

    # ---------------------------------------------
    # Send Email
    # ---------------------------------------------

    print("=" * 60)
    print("Resending verification email to:", email)

    success, message = send_verification_email(
        email,
        verification_token,
    )

    print("Email Sent:", success)
    print("Email Service Message:", message)
    print("=" * 60)

    if not success:
        return (
            False,
            message,
        )

    return (
        True,
        "A new verification email has been sent.",
    )