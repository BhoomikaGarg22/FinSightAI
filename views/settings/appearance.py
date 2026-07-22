import streamlit as st

from utils.ui import page_header


THEMES = [
    "System",
    "Light",
    "Dark",
]

ACCENTS = [
    "Blue",
    "Green",
    "Purple",
    "Orange",
]


def safe_index(options, value):

    return options.index(value) if value in options else 0


def render_appearance():

    settings = st.session_state.settings

    page_header(
        "🎨 Appearance",
        "Personalize the look and feel of FinSight AI.",
    )

    left, right = st.columns(2)

    with left:

        settings["theme"] = st.selectbox(
            "Theme",
            THEMES,
            index=safe_index(
                THEMES,
                settings.get("theme"),
            ),
        )

        settings["accent_color"] = st.selectbox(
            "Accent Color",
            ACCENTS,
            index=safe_index(
                ACCENTS,
                settings.get("accent_color"),
            ),
        )

    with right:

        settings["compact_dashboard"] = st.checkbox(
            "Compact Dashboard",
            value=settings.get(
                "compact_dashboard",
                False,
            ),
        )

        settings["animations"] = st.checkbox(
            "Enable Animations",
            value=settings.get(
                "animations",
                True,
            ),
        )

    st.caption(
        "Appearance settings are applied the next time the application loads."
    )