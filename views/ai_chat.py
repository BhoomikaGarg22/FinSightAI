import streamlit as st
from utils.navigation import navigate
from backend.api import chat_with_ai

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
    # REPORT CONTEXT
    # =====================================================

    if st.session_state.get("report_uploaded", False):
        st.success("Financial report loaded successfully.")
        st.info("Your uploaded report is available for questions.")
    # =====================================================
    # CHAT WINDOW
    # =====================================================

    #
    # =====================================================
    # CHAT INPUT
    # =====================================================

    question = st.chat_input(
        placeholder="Ask about stocks, earnings, valuation or market trends..."
    )

    if question:

        with st.container(border=True):

            st.subheader("Conversation")

            st.chat_message("user").write(question)

            with st.chat_message("assistant"):

                with st.spinner("Thinking..."):

                    answer = chat_with_ai(question)

                st.write(answer)

    


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
              company=st.session_state.get("company")
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