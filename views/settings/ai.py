import streamlit as st

from utils.ui import page_header


AI_STYLES = [
    "Balanced",
    "Conservative",
    "Aggressive",
]

RESPONSE_LENGTH = [
    "Short",
    "Medium",
    "Detailed",
]

REGIONS = [
    "Global",
    "India",
    "United States",
]

DASHBOARDS = [
    "Overview",
    "Portfolio",
    "Markets",
    "Watchlist",
]


def safe_index(options, value):

    return options.index(value) if value in options else 0


def render_ai():

    settings = st.session_state.settings

    page_header(
        "🤖 AI Preferences",
        "Customize how FinSight AI responds to you.",
    )

    left, right = st.columns(2)

    with left:

        settings["ai_style"] = st.selectbox(
            "AI Style",
            AI_STYLES,
            index=safe_index(
                AI_STYLES,
                settings.get("ai_style"),
            ),
        )

        settings["response_length"] = st.selectbox(
            "Response Length",
            RESPONSE_LENGTH,
            index=safe_index(
                RESPONSE_LENGTH,
                settings.get("response_length"),
            ),
        )

    with right:

        settings["preferred_region"] = st.selectbox(
            "Preferred Region",
            REGIONS,
            index=safe_index(
                REGIONS,
                settings.get("preferred_region"),
            ),
        )

        settings["default_dashboard"] = st.selectbox(
            "Default Dashboard",
            DASHBOARDS,
            index=safe_index(
                DASHBOARDS,
                settings.get("default_dashboard"),
            ),
        )

    st.info(
        "These preferences influence AI-generated insights and recommendations."
    )