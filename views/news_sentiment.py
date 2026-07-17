import streamlit as st
import pandas as pd
import plotly.express as px
import time
from data.companies import companies
def show_news_sentiment():

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown("""
    <div class="page-header">

    <h1>📰 AI News & Market Sentiment</h1>

    <p>
    Discover how AI interprets the latest financial news,
    market events, and investor sentiment.
    </p>

    <div class="market-status">

    🟢 <b>Live News Feed</b>

    <span class="status-dot"></span>

    Updated every few minutes

    </div>

    </div>
    """,
    unsafe_allow_html=True)

    # =====================================================
# SEARCH
# =====================================================

    st.markdown("##### 🔍 Search Company or Ticker")

    col1, col2 = st.columns([6, 1], vertical_alignment="bottom")

    with col1:
        company = st.text_input(
            "",
            value=st.session_state.get("company", "Apple"),
            label_visibility="collapsed",
            placeholder="Apple, Tesla, NVIDIA..."
        )
        if company:
            st.session_state["company"] = company

    with col2:
        analyze = st.button(
            "🔍 Analyze",
            key="news_analyze",
            use_container_width=True
        )

    if analyze:
        with st.spinner("Analyzing latest news..."):
            time.sleep(2)

        st.success("News analysis complete!")

    st.write("")

    # =====================================================
    # SENTIMENT OVERVIEW
    # =====================================================

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.metric(
                "Overall Sentiment",
                "🟢 Bullish"
            )

    with c2:
        with st.container(border=True):
            st.metric(
                "Confidence",
                "91%"
            )

    with c3:
        with st.container(border=True):
            st.metric(
                "Articles Analyzed",
                "128"
            )

    st.write("")
    st.info(
    "🤖 AI Confidence: **91%** • Based on 128 recent financial articles from trusted sources."
)
    # =====================================================
    # NEWS + CHART
    # =====================================================

    # =====================================================
# LATEST NEWS
# =====================================================

    with st.container(border=True):

        st.subheader("📰 Latest Financial News")

    # News Cards Here
    # =====================================================
# SENTIMENT TREND
# =====================================================

    with st.container(border=True):

        st.subheader("📈 Sentiment Trend")

    # Plotly Chart Here
        st.write("")

    # =====================================================
# AI MARKET ANALYSIS
# =====================================================

    st.divider()

    st.markdown("## 🤖 AI Market Analysis")

    st.caption(
        "AI-generated summary based on recent financial news and market sentiment."
    )

    with st.container(border=True):

        st.markdown("### 🟢 Overall Sentiment")

        st.markdown("## **BULLISH**")

        st.write(
            """
    Recent financial news indicates continued optimism around the technology sector.

    Positive earnings reports, increasing AI adoption, and strong institutional
    interest continue to support investor confidence.

    Overall market sentiment remains favorable, although investors should remain
    aware of macroeconomic uncertainty and elevated market valuations.
    """
        )

        st.markdown("---")

        c1, c2 = st.columns(2)

        with c1:

            st.markdown("### ✅ Key Drivers")

            st.markdown("""
    - Strong quarterly earnings

    - AI investments accelerating

    - Positive analyst ratings

    - Healthy revenue growth
    """)

        with c2:

            st.markdown("### ⚠ Risks")

            st.markdown("""
    - High valuation

    - Interest rate uncertainty

    - Market volatility

    - Global economic slowdown
    """)

    st.write("")

    # =====================================================
    # QUICK ACTIONS
    # =====================================================

    with st.container(border=True):

        st.subheader("⚡ Quick Actions")

        b1, b2, b3 = st.columns(3)

        with b1:
         st.button(
            "📈 Open Stock Analysis",
            key="view_stock",
            use_container_width=True
        )

        with b2:
         st.button(
            "💬 Chat with AI",
            key="news_ai",
            use_container_width=True
        )

        with b3:
         if st.button(
            "📄 Export Summary",
            use_container_width=True
        ):
            with st.spinner("Generating report..."):
                time.sleep(2)

            st.success("Summary exported successfully!")

    st.divider()

    left, right = st.columns([3, 1])

    with left:
        st.caption(
            "© 2026 FinSight AI • AI-Powered Financial Research Platform"
        )

    with right:
        st.caption("Version 1.0")