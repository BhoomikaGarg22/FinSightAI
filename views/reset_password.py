import streamlit as st

from backend.services.reset_password_service import (
    reset_password,
)

from backend.services.validation_service import (
    validate_password,
)


# =====================================================
# Reset Password Page
# =====================================================

def show_reset_password():

    token = st.query_params.get("reset")

    st.title("🔒 Reset Password")

    if not token:

        st.error("Invalid or missing password reset link.")

        if st.button(
            "Back to Login",
            use_container_width=True,
        ):
            st.query_params.clear()
            st.session_state.auth_page = "login"
            st.rerun()

        return

    st.write(
        """
Choose a strong password.

Your password must contain:

- At least 8 characters
- One uppercase letter
- One lowercase letter
- One number
"""
    )

    new_password = st.text_input(
        "New Password",
        type="password",
        key="reset_password",
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password",
        key="reset_confirm_password",
    )

    if st.button(
        "Reset Password",
        use_container_width=True,
        type="primary",
    ):

        if not new_password or not confirm_password:

            st.error("Please fill in all fields.")
            return

        if new_password != confirm_password:

            st.error("Passwords do not match.")
            return

        # Reuse the same password validation rules
        valid, error = validate_password(
            new_password,
        )

        if not valid:

            st.error(error)
            return

        with st.spinner("Updating password..."):

            success, message = reset_password(
                token,
                new_password,
            )

        if success:

            st.query_params.clear()

            st.success(message)

            st.balloons()

            st.info(
                """
Your password has been updated successfully.

You can now log in using your new password.
"""
            )

            if st.button(
                "Go to Login",
                use_container_width=True,
            ):

                st.session_state.auth_page = "login"
                st.rerun()

        else:

            st.error(message)

            if st.button(
                "Back to Login",
                use_container_width=True,
            ):

                st.query_params.clear()
                st.session_state.auth_page = "login"
                st.rerun()