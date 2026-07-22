import streamlit as st

from utils.ui import page_header


def render_notifications():

    settings = st.session_state.settings

    notifications = settings.setdefault(
        "notifications",
        {},
    )

    page_header(
        "🔔 Notifications",
        "Choose which alerts you want to receive.",
    )

    left, right = st.columns(2)

    with left:

        notifications["daily_summary"] = st.checkbox(
            "Daily Summary",
            value=notifications.get(
                "daily_summary",
                True,
            ),
        )

        notifications["market_news"] = st.checkbox(
            "Market News",
            value=notifications.get(
                "market_news",
                True,
            ),
        )

        notifications["earnings"] = st.checkbox(
            "Earnings Alerts",
            value=notifications.get(
                "earnings",
                True,
            ),
        )

    with right:

        notifications["price_alerts"] = st.checkbox(
            "Price Alerts",
            value=notifications.get(
                "price_alerts",
                False,
            ),
        )

        notifications["ai_alerts"] = st.checkbox(
            "AI Alerts",
            value=notifications.get(
                "ai_alerts",
                False,
            ),
        )

        notifications["weekly_ai"] = st.checkbox(
            "Weekly AI Report",
            value=notifications.get(
                "weekly_ai",
                False,
            ),
        )