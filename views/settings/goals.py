import streamlit as st

from utils.ui import page_header


GOALS = [
    "Retirement",
    "Emergency Fund",
    "Wealth Creation",
    "Passive Income",
    "House",
    "Car",
    "Education",
    "Travel",
]


def render_goals():

    settings = st.session_state.settings

    page_header(
        "🎯 Investment Goals",
        "Select the financial goals that matter most to you.",
    )

    selected = st.multiselect(
        "Goals",
        GOALS,
        default=settings.get("investment_goals", []),
    )

    settings["investment_goals"] = selected

    if selected:

        st.success(
            f"{len(selected)} goal(s) selected."
        )

    else:

        st.info(
            "Select one or more goals to help the AI personalize suggestions."
        )