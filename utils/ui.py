import streamlit as st


def page_header(title: str, subtitle: str = ""):
    st.markdown(
        f"""
        <div style="
            padding:22px;
            border-radius:16px;
            border:1px solid #2d3748;
            background-color:#111827;
            margin-bottom:20px;
        ">
            <h2 style="margin-bottom:6px;">{title}</h2>
            <p style="color:#9CA3AF;margin:0;">
                {subtitle}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section(title):
    st.markdown(f"### {title}")