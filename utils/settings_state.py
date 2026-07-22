import streamlit as st

from backend.config.profile_defaults import get_default_profile


def initialize_settings():

    if "settings" not in st.session_state:

        profile = (
            st.session_state.get("user", {})
            .get("profile")
        )

        if profile:

            merged = get_default_profile()

            for key, value in profile.items():
                merged[key] = value

            st.session_state.settings = merged

        else:

            st.session_state.settings = get_default_profile()

    if "settings_tab" not in st.session_state:
        st.session_state.settings_tab = "Personal"