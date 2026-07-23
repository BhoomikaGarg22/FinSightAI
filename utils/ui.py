import streamlit as st


def page_header(title: str, subtitle: str = ""):
    st.markdown(
        f"""
        <div style="
            padding:22px;
            border-radius:16px;
            border:1px solid #E5E7EB;
            background:#F8FAFC;
            margin-bottom:20px;
        ">
            <h2 style="margin-bottom:6px;color:#111827;">
                {title}
            </h2>
            <p style="color:#6B7280;margin:0;">
                {subtitle}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section(title):
    st.markdown(f"### {title}")