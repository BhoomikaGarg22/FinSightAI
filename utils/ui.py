
import streamlit as st


def page_header(title: str, subtitle: str = ""):

    settings = st.session_state.get("settings", {})
    theme = settings.get("theme", "System")

    st.markdown(
        f"""
        <div class="finsight-page-header" data-theme="{theme.lower()}">
            <h2>{title}</h2>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section(title):
    st.markdown(f"### {title}")
