import streamlit as st

from utils.ui import page_header


INVESTOR_TYPES = [
    "Investor",
    "Trader",
    "Both",
]

RISK_LEVELS = [
    "Low",
    "Moderate",
    "High",
]

EXPERIENCE = [
    "Beginner",
    "Intermediate",
    "Advanced",
]

HORIZONS = [
    "Short Term",
    "Medium Term",
    "Long Term",
]


def safe_index(options, value):

    if value in options:
        return options.index(value)

    return 0


def render_investor():

    settings = st.session_state.settings

    page_header(
        "📈 Investor Profile",
        "These settings personalize AI recommendations.",
    )

    col1, col2 = st.columns(2)

    with col1:

        settings["investor_type"] = st.selectbox(
            "Investor Type",
            INVESTOR_TYPES,
            index=safe_index(
                INVESTOR_TYPES,
                settings.get("investor_type"),
            ),
        )

        settings["risk_appetite"] = st.selectbox(
            "Risk Appetite",
            RISK_LEVELS,
            index=safe_index(
                RISK_LEVELS,
                settings.get("risk_appetite"),
            ),
        )

    with col2:

        settings["investment_experience"] = st.selectbox(
            "Investment Experience",
            EXPERIENCE,
            index=safe_index(
                EXPERIENCE,
                settings.get("investment_experience"),
            ),
        )

        settings["investment_horizon"] = st.selectbox(
            "Investment Horizon",
            HORIZONS,
            index=safe_index(
                HORIZONS,
                settings.get("investment_horizon"),
            ),
        )

    st.info(
        "These preferences are used by FinSight AI to personalize "
        "market insights and recommendations."
    )