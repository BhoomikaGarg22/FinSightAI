import streamlit as st
from streamlit_option_menu import option_menu

# Import pages
from views.dashboard import show_dashboard
from views.stock_analysis import show_stock_analysis
from views.report_analyzer import show_report_analyzer
from views.news_sentiment import show_news_sentiment
from views.ai_chat import show_ai_chat
from views.settings import show_settings

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="FinSight AI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("📈 FinSight AI")

    selected = option_menu(
        menu_title=None,
        options=[
            "Dashboard",
            "Stock Analysis",
            "Report Analyzer",
            "News & Sentiment",
            "AI Chat",
            "Settings"
        ],
        icons=[
            "speedometer2",
            "graph-up-arrow",
            "file-earmark-text",
            "newspaper",
            "chat-dots",
            "gear"
        ],
        default_index=0,
    )

# -----------------------------
# Routing
# -----------------------------
if selected == "Dashboard":
    show_dashboard()

elif selected == "Stock Analysis":
    show_stock_analysis()

elif selected == "Report Analyzer":
    show_report_analyzer()

elif selected == "News & Sentiment":
    show_news_sentiment()

elif selected == "AI Chat":
    show_ai_chat()

elif selected == "Settings":
    show_settings()