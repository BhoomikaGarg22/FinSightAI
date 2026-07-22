import uuid

from backend.services.auth_service import (
    create_user,
    login_user
)

# -------------------------
# Generate unique email
# -------------------------
email = f"{uuid.uuid4().hex[:8]}@test.com"

# -------------------------
# Test User Registration
# -------------------------
success, message = create_user(
    name="Aditi",
    email=email,
    password="Password123"
)

assert success, f"Signup failed: {message}"

# -------------------------
# Test User Login
# -------------------------
success, user = login_user(
    email=email,
    password="Password123"
)

assert success, "Login failed."

assert user["name"] == "Aditi"
assert user["email"] == email

print("✅ Authentication tests passed successfully!")