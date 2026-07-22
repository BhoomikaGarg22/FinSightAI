"""
Email Service
-------------

Handles sending emails for:

- Email verification
- Password reset
- Future notifications
"""

import os
import smtplib
import ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = os.getenv("BREVO_SMTP_SERVER")
SMTP_PORT = int(os.getenv("BREVO_SMTP_PORT", "587"))

# SMTP Authentication
EMAIL = os.getenv("BREVO_EMAIL")
PASSWORD = os.getenv("BREVO_PASSWORD")

# Verified sender email
SENDER_EMAIL = os.getenv("BREVO_SENDER_EMAIL")

APP_URL = os.getenv("APP_URL")


# =====================================================
# Configuration
# =====================================================

def _check_configuration():
    """
    Ensure required environment variables exist.
    """

    required = {
        "BREVO_SMTP_SERVER": SMTP_SERVER,
        "BREVO_SMTP_PORT": SMTP_PORT,
        "BREVO_EMAIL": EMAIL,
        "BREVO_PASSWORD": PASSWORD,
        "BREVO_SENDER_EMAIL": SENDER_EMAIL,
        "APP_URL": APP_URL,
    }

    missing = [
        key
        for key, value in required.items()
        if value in (None, "")
    ]

    if missing:
        raise ValueError(
            f"Missing environment variables: {', '.join(missing)}"
        )


# =====================================================
# Generic Email Sender
# =====================================================

def _send_email(
    receiver_email: str,
    subject: str,
    plain_text: str,
    html: str,
):
    """
    Generic SMTP sender.
    """

    try:

        _check_configuration()

        message = MIMEMultipart("alternative")

        message["Subject"] = subject
        message["From"] = SENDER_EMAIL
        message["To"] = receiver_email

        message.attach(
            MIMEText(
                plain_text,
                "plain",
            )
        )

        message.attach(
            MIMEText(
                html,
                "html",
            )
        )

        context = ssl.create_default_context()

        with smtplib.SMTP(
            SMTP_SERVER,
            SMTP_PORT,
        ) as server:

            server.starttls(context=context)

            server.login(
                EMAIL,
                PASSWORD,
            )
            print("SMTP Login:", EMAIL)
            print("Sender:", SENDER_EMAIL)
            print("Recipient:", receiver_email)
            print("Message From:", message["From"])
            
            server.sendmail(
                SENDER_EMAIL,
                receiver_email,
                message.as_string(),
            )

        print(f"✅ Email sent successfully to {receiver_email}")

        return True, "Email sent successfully."

    except Exception as e:

        print("❌ Email Error:", e)

        return False, str(e)


# =====================================================
# Verification Email
# =====================================================

def send_verification_email(
    receiver_email: str,
    token: str,
):

    verify_link = f"{APP_URL}?verify={token}"

    subject = "Verify your FinSight AI Account"

    plain_text = f"""
Welcome to FinSight AI!

Verify your account by opening the link below:

{verify_link}

If you didn't create this account,
you can safely ignore this email.
"""

    html = f"""
<!DOCTYPE html>
<html>
<body style="background:#f5f7fb;padding:40px;font-family:Arial,sans-serif;">

<div style="max-width:650px;margin:auto;background:white;padding:40px;border-radius:12px;box-shadow:0 4px 12px rgba(0,0,0,.08);">

<h1 style="color:#2563eb;">📈 FinSight AI</h1>

<h2>Verify your email</h2>

<p>
Welcome to <b>FinSight AI</b>.
</p>

<p>
Please verify your email before logging in.
</p>

<p style="margin:35px 0;">

<a
href="{verify_link}"
style="
background:#2563eb;
color:white;
padding:14px 26px;
text-decoration:none;
border-radius:8px;
font-weight:bold;
">

Verify Email

</a>

</p>

<p>
Or paste this link into your browser:
</p>

<p style="color:#2563eb;">
{verify_link}
</p>

<hr>

<p style="color:gray;font-size:14px;">
If you didn't create this account, you can safely ignore this email.
</p>

</div>

</body>
</html>
"""

    return _send_email(
        receiver_email,
        subject,
        plain_text,
        html,
    )


# =====================================================
# Password Reset Email
# =====================================================

def send_reset_password_email(
    receiver_email: str,
    token: str,
):

    reset_link = f"{APP_URL}?reset={token}"

    subject = "Reset your FinSight AI Password"

    plain_text = f"""
A request was made to reset your FinSight AI password.

Reset your password using the link below:

{reset_link}

This link expires in 1 hour.

If you didn't request this password reset,
you can safely ignore this email.
"""

    html = f"""
<!DOCTYPE html>
<html>
<body style="background:#f5f7fb;padding:40px;font-family:Arial,sans-serif;">

<div style="max-width:650px;margin:auto;background:white;padding:40px;border-radius:12px;box-shadow:0 4px 12px rgba(0,0,0,.08);">

<h1 style="color:#2563eb;">📈 FinSight AI</h1>

<h2>Reset Your Password</h2>

<p>
We received a request to reset your password.
</p>

<p>
Click the button below to choose a new password.
</p>

<p style="margin:35px 0;">

<a
href="{reset_link}"
style="
background:#dc2626;
color:white;
padding:14px 26px;
text-decoration:none;
border-radius:8px;
font-weight:bold;
">

Reset Password

</a>

</p>

<p>
Or paste this link into your browser:
</p>

<p style="color:#2563eb;">
{reset_link}
</p>

<hr>

<p style="color:gray;font-size:14px;">
This link expires in one hour.
</p>

<p style="color:gray;font-size:14px;">
If you didn't request a password reset,
you can safely ignore this email.
</p>

</div>

</body>
</html>
"""

    return _send_email(
        receiver_email,
        subject,
        plain_text,
        html,
    )