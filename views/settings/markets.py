import streamlit as st

from utils.ui import page_header


MARKETS = [
    "India",
    "United States",
    "Europe",
    "Japan",
    "China",
    "Crypto",
    "Forex",
    "Commodities",
]


def render_markets():

    settings = st.session_state.settings

    page_header(
        "🌍 Preferred Markets",
        "Choose the markets you want FinSight AI to prioritize.",
    )

    selected = st.multiselect(
        "Markets",
        MARKETS,
        default=settings.get("markets", []),
    )

    settings["markets"] = selected

    if selected:

        st.success(
            f"{len(selected)} market(s) selected."
        )

    else:

        st.info(
            "No preferred markets selected."
        )