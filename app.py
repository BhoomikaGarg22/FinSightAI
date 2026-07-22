import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="FinSight AI",
    page_icon="assets/images/icon_logo.png",
    layout="wide",
)

# --------------------------------------------------
# Initialize Session State
# --------------------------------------------------

if "theme" not in st.session_state:
    st.session_state.theme = "Light"

if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"

# --------------------------------------------------
# Load Global CSS
# --------------------------------------------------

theme = st.session_state.get("theme", "Light")

# Common CSS
with open("assets/css/common.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True,
    )

# Theme CSS
css_file = "assets/css/dark.css" if theme == "Dark" else "assets/css/light.css"

with open(css_file) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True,
    )

# --------------------------------------------------
# Initialize Database
# --------------------------------------------------

from backend.models.init_db import create_tables

if "db_initialized" not in st.session_state:
    create_tables()
    st.session_state.db_initialized = True

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"

if "auth_page" not in st.session_state:
    st.session_state.auth_page = "login"

# --------------------------------------------------
# Email Verification
# --------------------------------------------------

if "verify" in st.query_params:
    from views.verify_email import show_verify_page

    show_verify_page()
    st.stop()

# --------------------------------------------------
# Password Reset
# --------------------------------------------------

if "reset" in st.query_params:
    from views.reset_password import show_reset_password

    show_reset_password()
    st.stop()

# --------------------------------------------------
# Authentication
# --------------------------------------------------

if not st.session_state.logged_in:

    if st.session_state.auth_page == "forgot_password":
        from views.forgot_password import show_forgot_password

        show_forgot_password()

    else:
        from views.auth import show_auth

        show_auth()

    st.stop()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

from components.sidebar import show_sidebar

show_sidebar()

# --------------------------------------------------
# Routing
# --------------------------------------------------

current_page = st.session_state.current_page

if current_page == "Dashboard":

    from views.dashboard import show_dashboard

    show_dashboard()

elif current_page == "Stock Analysis":

    from views.stock_analysis_v2 import show_stock_analysis_v2

    show_stock_analysis_v2()

elif current_page == "Watchlist":

    from views.watchlist import show_watchlist

    show_watchlist()

elif current_page == "Report Analyzer":

    from views.report_analyzer import show_report_analyzer

    show_report_analyzer()

elif current_page == "News & Sentiment":

    from views.news_sentiment import show_news_sentiment

    show_news_sentiment()

elif current_page == "AI Chat":

    from views.ai_chat import show_ai_chat

    show_ai_chat()

elif current_page == "Settings":

    from views.settings_page import render_settings

    render_settings()