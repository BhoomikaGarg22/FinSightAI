import streamlit as st

from backend.services.verification_service import (
    verify_email,
)


def show_verify_page():
    """
    Display the email verification page.
    """

    token = st.query_params.get("verify")

    st.markdown(
        """
        <div style="text-align:center; margin-top:40px;">
            <h1>📧 Email Verification</h1>
            <p>FinSight AI Account Verification</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not token:

        st.error("❌ Invalid verification link.")

        if st.button(
            "← Back to Login",
            use_container_width=True,
        ):
            st.query_params.clear()
            st.rerun()

        return

    with st.spinner("Verifying your account..."):

        success = verify_email(token)

    if success:

        st.success("🎉 Your email has been verified successfully!")

        st.balloons()

        st.info(
            "You can now login using your email and password."
        )

    else:

        st.error(
            "This verification link is invalid, expired, or has already been used."
        )

    st.query_params.clear()

    if st.button(
        "Go to Login",
        type="primary",
        use_container_width=True,
    ):
        st.rerun()