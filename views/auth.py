import streamlit as st

from backend.services.auth_service import (
    create_user,
    login_user,
    resend_verification_email,
)


# =====================================================
# Session State
# =====================================================

def initialize_auth_state():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "user" not in st.session_state:
        st.session_state.user = None

    if "profile" not in st.session_state:
        st.session_state.profile = {}

    if "auth_mode" not in st.session_state:
        st.session_state.auth_mode = "login"

    if "auth_page" not in st.session_state:
        st.session_state.auth_page = "login"


# =====================================================
# Authentication Page
# =====================================================

def show_auth():

    initialize_auth_state()

    st.markdown(
        """
        <div style="text-align:center;padding-top:10px;">
            <h1>📈 FinSight AI</h1>
            <h4 style="color:gray;">
                AI Powered Financial Intelligence Platform
            </h4>
        </div>

        <br>
        """,
        unsafe_allow_html=True,
    )

    _, center, _ = st.columns([1, 2, 1])

    with center:

        login_tab, signup_tab = st.tabs(
            [
                "Login",
                "Create Account",
            ]
        )

        # =====================================================
        # LOGIN
        # =====================================================

        with login_tab:

            st.subheader("Welcome Back 👋")

            login_email = st.text_input(
                "Email",
                key="login_email",
            )

            login_password = st.text_input(
                "Password",
                type="password",
                key="login_password",
            )

            col1, col2 = st.columns([1, 1])

            with col2:
                if st.button(
                    "Forgot Password?",
                    key="forgot_password",
                    use_container_width=True,
                ):
                    st.session_state.auth_page = "forgot_password"
                    st.rerun()

            login_button = st.button(
                "Login",
                use_container_width=True,
                type="primary",
            )

            if login_button:

                if not login_email or not login_password:

                    st.error("Please fill in all fields.")

                else:

                    with st.spinner("Logging in..."):

                        success, result = login_user(
                            login_email,
                            login_password,
                        )

                    if success:

                        st.session_state.logged_in = True

                        # Store the complete user object
                        st.session_state.user = result

                        # Store profile separately
                        st.session_state.profile = result.get("profile", {})

                        st.rerun()

                    else:

                        st.error(result)

                        if "verify your email" in result.lower():

                            st.info(
                                "Didn't receive the verification email?"
                            )

                            if st.button(
                                "Resend Verification Email",
                                use_container_width=True,
                            ):

                                with st.spinner(
                                    "Sending verification email..."
                                ):

                                    resend_success, resend_message = (
                                        resend_verification_email(
                                            login_email
                                        )
                                    )

                                if resend_success:

                                    st.success(resend_message)

                                    st.info(
                                        """
A new verification email has been sent.

Please check your Inbox and Spam folder.
"""
                                    )

                                else:

                                    st.error(resend_message)

        # =====================================================
        # SIGN UP
        # =====================================================

        with signup_tab:

            st.subheader("Create Account")

            signup_name = st.text_input(
                "Full Name",
                key="signup_name",
            )

            signup_email = st.text_input(
                "Email",
                key="signup_email",
            )

            signup_password = st.text_input(
                "Password",
                type="password",
                key="signup_password",
                help="Minimum 8 characters including uppercase, lowercase and a number.",
            )

            confirm_password = st.text_input(
                "Confirm Password",
                type="password",
                key="signup_confirm",
            )

            signup_button = st.button(
                "Create Account",
                use_container_width=True,
            )

            if signup_button:

                if (
                    not signup_name
                    or not signup_email
                    or not signup_password
                    or not confirm_password
                ):

                    st.error("Please fill in all fields.")

                elif signup_password != confirm_password:

                    st.error("Passwords do not match.")

                else:

                    with st.spinner(
                        "Creating your account..."
                    ):

                        success, message = create_user(
                            name=signup_name,
                            email=signup_email,
                            password=signup_password,
                        )

                    if success:

                        st.success(
                            "🎉 Account created successfully!"
                        )

                        st.info(
                            """
We've sent a verification email to your inbox.

Please verify your email before logging in.

If you don't see the email within a minute, check your Spam folder.
"""
                        )

                    else:

                        st.error(message)