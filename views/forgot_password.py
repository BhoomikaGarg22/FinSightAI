import streamlit as st

from backend.services.reset_password_service import (
    request_password_reset,
)


# =====================================================
# Forgot Password Page
# =====================================================

def show_forgot_password():

    st.title("🔑 Forgot Password")

    st.write(
        """
Forgot your password?

Enter the email address associated with your account and we'll send you
a password reset link.
"""
    )

    email = st.text_input(
        "Email Address",
        placeholder="Enter your email",
    )

    reset_button = st.button(
        "Send Reset Link",
        use_container_width=True,
        type="primary",
    )

    if reset_button:

        if not email.strip():

            st.error("Please enter your email address.")

        else:

            with st.spinner("Sending password reset email..."):

                success, message = request_password_reset(
                    email
                )

            if success:

                st.success(message)

                st.info(
                    """
A password reset link has been sent to your email.

• Check your Inbox
• Check your Spam folder
• The link expires in **1 hour**
"""
                )

            else:

                st.error(message)

    st.divider()

    if st.button(
        "← Back to Login",
        use_container_width=True,
    ):

        st.session_state.auth_page = "login"
        st.rerun()