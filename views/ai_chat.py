import streamlit as st
from utils.navigation import navigate

def show_ai_chat():

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown("""
    <div class="page-header">

    <h1>AI Financial Assistant</h1>

    <p>
    Your AI-powered financial research companion.
    Analyze stocks, summarize reports, understand market trends,
    and receive intelligent investment insights.
    </p>

    <div class="market-status">

    <span class="status-dot"></span>

    <b>AI Assistant Online</b>
    </div>

    </div>
    """, unsafe_allow_html=True)
    st.caption(
        "Ask questions about stocks, financial reports, earnings, market trends, and investment opportunities."
    )

    st.write("")

    # =====================================================
    # SUGGESTED PROMPTS
    # =====================================================

    st.subheader("Suggested Questions")

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):
            st.markdown("### Analyze Apple's Q2 Earnings")
            st.caption("Revenue, profitability and AI outlook")

        with st.container(border=True):
            st.markdown("### Compare Tesla vs NVIDIA")
            st.caption("Growth, valuation and future potential")

    with col2:

        with st.container(border=True):
            st.markdown("### Market Outlook")
            st.caption("Summarize today's important events")

        with st.container(border=True):
            st.markdown("### Explain P/E Ratio")
            st.caption("Understand valuation metrics")

    st.write("")

    # =====================================================
    # CHAT WINDOW
    # =====================================================

    with st.container(border=True):

        st.subheader("Conversation")

        st.chat_message("user").write(
            "Should I invest in NVIDIA for the long term?"
        )

        with st.chat_message("assistant"):

         st.markdown("### Investment Summary")

         st.write(
          """
        NVIDIA continues to benefit from strong AI adoption,
        rapid data center expansion and cloud infrastructure demand.

        Overall fundamentals remain strong for long-term investors.
        """
           )

        st.divider()

        left, right = st.columns(2)

        with left:

          st.markdown("#### Strengths")

          st.markdown("""
        - Industry leader in AI chips
        - Strong revenue growth
        - Expanding cloud partnerships
        - High institutional confidence
        """)

        with right:

          st.markdown("#### Risks")

          st.markdown("""
        - Premium valuation
        - Increasing competition
        - Export restrictions
        - Market volatility
        """)

        
        st.divider()

        st.markdown("#### Analysis Overview")

        c1, c2, c3 = st.columns(3)

        with c1:
         st.metric(
          "Market Sentiment",
          "Bullish"
         )

        with c2:
         st.metric(
          "Risk Level",
          "Moderate"
         )

        with c3:
         st.metric(
          "Time Horizon",
          "Long-Term"
         )

        st.divider()

        c1, c2 = st.columns(2)

        with c1:

         with st.container(border=True):

            st.metric(
                "Recommendation",
                "BUY"
            )

        with c2:

         with st.container(border=True):

            st.metric(
                "Confidence",
                "91%"
            )

        st.divider()

        st.caption("Sources")

        st.caption("Sources")

        st.markdown("""
        - Yahoo Finance
        - SEC Filings
        - Reuters
        - Company Earnings Report
        """)

    st.write("")

    # =====================================================
    # CHAT INPUT
    # =====================================================

    st.chat_input(
        placeholder="Ask about stocks, earnings, valuation or market trends..."
    )

    st.write("")


    # =====================================================
    # QUICK ACTIONS
    # =====================================================

    with st.container(border=True):

        st.subheader("Quick Actions")

        b1, b2, b3 = st.columns(3)

        with b1:
         if st.button(
          "Analyze Stock",
          use_container_width=True
        ):
            navigate(
             "Stock Analysis",
              company=company
            )

        with b2:
         if st.button(
          "Financial Report",
          use_container_width=True
        ):
            navigate("Report Analyzer")

        with b3:
         if st.button(
          "Market News",
          use_container_width=True
        ):
            navigate("News & Sentiment")

    st.divider()

    st.caption("© 2026 FinSight AI | AI-Powered Financial Research Platform")