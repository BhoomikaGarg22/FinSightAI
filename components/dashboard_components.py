import streamlit as st


def section_title(title, subtitle=""):
    st.markdown(
        f"""
        <div class="section-title">{title}</div>
        <div class="section-subtitle">{subtitle}</div>
        """,
        unsafe_allow_html=True,
    )


def info_card(title, content):

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <br>
            <div style="font-size:16px; line-height:1.7;">
                {content}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )