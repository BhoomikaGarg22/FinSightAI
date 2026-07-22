import streamlit as st

from utils.settings_state import initialize_settings
from utils.ui import page_header

from views.settings.navigation import render_navigation

from views.settings.personal import render_personal
from views.settings.investor import render_investor
from views.settings.goals import render_goals
from views.settings.markets import render_markets
from views.settings.ai import render_ai
from views.settings.notifications import render_notifications
from views.settings.appearance import render_appearance
from views.settings.account import render_account
from views.settings.security import render_security
from views.settings.actions import render_actions


PAGES = {
    "Personal": render_personal,
    "Investor": render_investor,
    "Goals": render_goals,
    "Markets": render_markets,
    "AI": render_ai,
    "Notifications": render_notifications,
    "Appearance": render_appearance,
    "Account": render_account,
    "Security": render_security,
}


def render_settings():

    initialize_settings()

    user = st.session_state.get("user", {})
    settings = st.session_state.settings

    username = (
        user.get("username")
        or user.get("email", "User").split("@")[0]
    )

    page_header(
        "⚙️ Settings",
        "Manage your account, preferences and AI experience.",
    )

    with st.container(border=True):

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "User",
            username,
        )

        col2.metric(
            "Country",
            settings.get("country"),
        )

        col3.metric(
            "Currency",
            settings.get("currency"),
        )

    st.write("")

    left, right = st.columns([1, 3], gap="large")

    with left:

        render_navigation()

    with right:

        page = st.session_state.settings_tab

        PAGES[page]()

        st.divider()

        render_actions()