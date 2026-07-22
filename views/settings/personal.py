import streamlit as st

from utils.ui import page_header


LANGUAGES = [
    "English",
    "Hindi",
]

CURRENCIES = [
    "USD",
    "INR",
]


def safe_index(options, value):

    if value in options:
        return options.index(value)

    return 0


def render_personal():

    settings = st.session_state.settings

    page_header(
        "👤 Personal Information",
        "Manage your personal and regional preferences.",
    )

    left, right = st.columns(2)

    with left:

        settings["display_name"] = st.text_input(
            "Display Name",
            value=settings.get("display_name", ""),
            placeholder="e.g. Aditi",
        )

        settings["phone"] = st.text_input(
            "Phone Number",
            value=settings.get("phone", ""),
        )

        settings["country"] = st.text_input(
            "Country",
            value=settings.get("country", ""),
        )

        settings["occupation"] = st.text_input(
            "Occupation",
            value=settings.get("occupation", ""),
        )

    with right:

        settings["language"] = st.selectbox(
            "Language",
            LANGUAGES,
            index=safe_index(
                LANGUAGES,
                settings.get("language"),
            ),
        )

        settings["currency"] = st.selectbox(
            "Currency",
            CURRENCIES,
            index=safe_index(
                CURRENCIES,
                settings.get("currency"),
            ),
        )