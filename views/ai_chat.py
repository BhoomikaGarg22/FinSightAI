import streamlit as st


def show_ai_chat():

    # =====================================================
    # HEADER
    # =====================================================

    st.title("🤖 AI Financial Assistant")
    st.caption(
        "Ask questions about stocks, financial reports, earnings, market trends, and investment opportunities."
    )

    st.write("")

    # =====================================================
    # SUGGESTED PROMPTS
    # =====================================================

    st.subheader("💡 Suggested Prompts")

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):
            st.write("📈 Analyze Apple's latest quarterly earnings")

        with st.container(border=True):
            st.write("📊 Compare Tesla and NVIDIA")

    with c2:
        with st.container(border=True):
            st.write("📰 Summarize today's market news")

        with st.container(border=True):
            st.write("⚠ What are Microsoft's biggest risks?")

    st.write("")

    # =====================================================
    # CHAT WINDOW
    # =====================================================

    with st.container(border=True):

        st.subheader("💬 Conversation")

        st.chat_message("user").write(
            "Should I invest in NVIDIA for the long term?"
        )

        st.chat_message("assistant").write(
            """
NVIDIA continues to benefit from strong AI demand,
cloud computing growth, and data center expansion.

### Strengths

• Industry leader in AI chips

• Excellent revenue growth

• Strong institutional support

### Risks

• Premium valuation

• Increasing competition

### Recommendation

**Long-term outlook remains Bullish.**

Confidence: **91%**
"""
        )

    st.write("")

    # =====================================================
    # CHAT INPUT
    # =====================================================

    st.chat_input(
        "Ask anything about stocks, reports or market trends..."
    )

    st.write("")


    # =====================================================
    # QUICK ACTIONS
    # =====================================================

    with st.container(border=True):

        st.subheader("⚡ Quick Actions")

        b1, b2, b3 = st.columns(3)

        with b1:
            st.button(
                "📄 Ask About Report",
                key="chat_report",
                use_container_width=True
            )

        with b2:
            st.button(
                "📈 Analyze Stock",
                key="chat_stock",
                use_container_width=True
            )

        with b3:
            st.button(
                "📰 Market News",
                key="chat_news",
                use_container_width=True
            )

    st.divider()

    st.caption("© 2026 FinSight AI | AI-Powered Financial Research Platform")