from views.stock_analysis_v2 import show_stock_analysis_v2
import streamlit as st
from views.watchlist import show_watchlist
# -----------------------------------
# Page Config
# -----------------------------------
st.set_page_config(
    page_title="FinSight AI",
    page_icon="assets/images/icon_logo.png",
    layout="wide"
)

# -----------------------------------
# Load CSS
# -----------------------------------
with open("assets/css/common.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------------
# Imports
# -----------------------------------
from components.sidebar import show_sidebar

from views.dashboard import show_dashboard
from views.stock_analysis_v2 import show_stock_analysis_v2
from views.report_analyzer import show_report_analyzer
from views.news_sentiment import show_news_sentiment
from views.ai_chat import show_ai_chat
from views.settings import show_settings

# -----------------------------------
# Sidebar
# -----------------------------------
# -----------------------------------
# Sidebar
# -----------------------------------

show_sidebar()

current_page = st.session_state.current_page
# -----------------------------------
# Routing
# -----------------------------------
if current_page == "Dashboard":
    show_dashboard()

elif current_page == "Stock Analysis":
    show_stock_analysis_v2()

elif current_page == "Watchlist":
    show_watchlist()

elif current_page == "Report Analyzer":
    show_report_analyzer()

elif current_page == "News & Sentiment":
    show_news_sentiment()

elif current_page == "AI Chat":
    show_ai_chat()

elif current_page == "Settings":
    show_settings()