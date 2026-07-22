import streamlit as st

from backend.services.auth_service import update_user_profile


def render_actions():

    st.divider()

    left, right = st.columns(2)

    with left:

        if st.button(
            "💾 Save Settings",
            type="primary",
            use_container_width=True,
        ):

            success = update_user_profile(
                st.session_state.user["id"],
                st.session_state.settings,
            )

            if success:

                st.session_state.user["profile"] = (
                    st.session_state.settings.copy()
                )

                st.toast(
                    "Settings Saved ✅"
                )

                st.success(
                    "Your preferences have been updated."
                )

            else:

                st.error(
                    "Unable to save settings."
                )

    with right:

        if st.button(
            "↺ Reset",
            use_container_width=True,
        ):

            if "profile" in st.session_state.user:

                st.session_state.settings = (
                    st.session_state.user["profile"].copy()
                )

            st.rerun()