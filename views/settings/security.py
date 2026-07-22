import streamlit as st

from utils.ui import page_header


def render_security():

    page_header(
        "🔒 Security",
        "Manage your account security.",
    )

    with st.form("password_form"):

        current = st.text_input(
            "Current Password",
            type="password",
        )

        new = st.text_input(
            "New Password",
            type="password",
        )

        confirm = st.text_input(
            "Confirm Password",
            type="password",
        )

        submitted = st.form_submit_button(
            "Update Password",
            use_container_width=True,
        )

        if submitted:

            if not current or not new or not confirm:

                st.warning(
                    "Please complete all fields."
                )

            elif new != confirm:

                st.error(
                    "Passwords do not match."
                )

            else:

                st.success(
                    "Backend password update can be connected here."
                )

    st.divider()

    st.subheader("Other Actions")

    st.button(
        "Logout from all devices",
        use_container_width=True,
    )