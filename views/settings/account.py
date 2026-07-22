import streamlit as st

from utils.ui import page_header


def render_account():

    page_header(
        "👤 Account",
        "View your account information.",
    )

    user = st.session_state.get("user", {})
    settings = st.session_state.get("settings", {})

    username = (
        user.get("username")
        or user.get("email", "User").split("@")[0]
    )

    email = user.get("email", "Not Available")

    created = user.get(
        "created_at",
        "Not Available",
    )

    verified = (
        "✅ Verified"
        if user.get("is_verified")
        else "❌ Not Verified"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.text_input(
            "Username",
            value=username,
            disabled=True,
        )

        st.text_input(
            "Email",
            value=email,
            disabled=True,
        )

        st.text_input(
            "Country",
            value=settings.get("country", ""),
            disabled=True,
        )

    with col2:

        st.text_input(
            "Created",
            value=str(created),
            disabled=True,
        )

        st.text_input(
            "Verification",
            value=verified,
            disabled=True,
        )

        st.text_input(
            "Currency",
            value=settings.get("currency", ""),
            disabled=True,
        )

    st.divider()

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Risk",
        settings.get(
            "risk_appetite",
            "-",
        ),
    )

    c2.metric(
        "Experience",
        settings.get(
            "investment_experience",
            "-",
        ),
    )

    c3.metric(
        "Investor",
        settings.get(
            "investor_type",
            "-",
        ),
    )