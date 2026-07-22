import os
import ssl
import smtplib
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

print("=" * 50)
print("EMAIL:", repr(os.getenv("BREVO_EMAIL")))
print("SERVER:", repr(os.getenv("BREVO_SMTP_SERVER")))
print("PORT:", repr(os.getenv("BREVO_SMTP_PORT")))

password = os.getenv("BREVO_PASSWORD")
print("PASSWORD PREFIX:", password[:10])
print("PASSWORD LENGTH:", len(password))
print("=" * 50)

server = smtplib.SMTP(
    os.getenv("BREVO_SMTP_SERVER"),
    int(os.getenv("BREVO_SMTP_PORT")),
)

server.starttls(context=ssl.create_default_context())

print("Attempting login...")

server.login(
    os.getenv("BREVO_EMAIL"),
    password,
)

print("✅ Login successful!")

server.quit()