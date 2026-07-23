import streamlit as st


SECTIONS = [
    "Personal",
    "Investor",
    "Goals",
    "Markets",
    "AI",
    "Notifications",
    "Appearance",
    "Account",
    "Security",
]

ICONS = {
    "Personal": "👤",
    "Investor": "📈",
    "Goals": "🎯",
    "Markets": "🌍",
    "AI": "🤖",
    "Notifications": "🔔",
    "Appearance": "🎨",
    "Account": "🪪",
    "Security": "🔒",
}


def render_navigation():

    st.markdown("## ⚙️ Preferences")

    for page in SECTIONS:

        button_type = (
            "primary"
            if st.session_state.settings_tab == page
            else "secondary"
        )

        if st.button(
            f"{ICONS[page]}  {page}",
            use_container_width=True,
            type=button_type,
        ):
            st.session_state.settings_tab = page
            st.rerun()