from views.stock_analysis_v2 import show_stock_analysis_v2
import streamlit as st

# -----------------------------------
# Page Config
# -----------------------------------
st.set_page_config(
    page_title="FinSight AI",
    page_icon="📈",
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
from views.stock_analysis import show_stock_analysis
from views.report_analyzer import show_report_analyzer
from views.news_sentiment import show_news_sentiment
from views.ai_chat import show_ai_chat
from views.settings import show_settings

# -----------------------------------
# Sidebar
# -----------------------------------
selected = show_sidebar()

# -----------------------------------
# Routing
# -----------------------------------
if selected == "Dashboard":
    show_dashboard()

elif selected == "Stock Analysis":
    show_stock_analysis_v2()

elif selected == "Report Analyzer":
    show_report_analyzer()

elif selected == "News & Sentiment":
    show_news_sentiment()

elif selected == "AI Chat":
    show_ai_chat()

elif selected == "Settings":
    show_settings()