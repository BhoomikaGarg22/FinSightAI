import streamlit as st

from utils.navigation import navigate
from backend.api import chat_with_ai

from backend.services.chatbot_service import (
    save_chat,
    get_chat_history,
    clear_history,
)


def show_ai_chat():

    # ------------------------------------
    # Session State
    # ------------------------------------

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # ------------------------------------
    # Header
    # ------------------------------------

    st.markdown(
        """
        <div class="page-header">

        <h1>AI Financial Assistant</h1>

        <p>
        Your AI-powered financial research companion.
        Analyze stocks, summarize reports,
        understand market trends,
        and receive intelligent investment insights.
        </p>

        <div class="market-status">
            <span class="status-dot"></span>
            <b>AI Assistant Online</b>
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption(
        "Ask questions about stocks, reports, valuation and markets."
    )

    # ------------------------------------
    # Sidebar History
    # ------------------------------------

    with st.expander("📜 Chat History"):

        history = get_chat_history(
            st.session_state.user["id"]
        )

        if history:

            for chat in history:

                st.markdown(
                    f"""
                    **Q:** {chat["question"]}

                    **A:** {chat["answer"]}

                    ---
                    """
                )

        else:
            st.info("No previous chats.")

        if st.button(
            "🗑 Clear History",
            width="stretch",
        ):
            clear_history(
                st.session_state.user["id"]
            )

            st.success("History cleared.")

            st.rerun()

    st.divider()

    # ------------------------------------
    # Previous Conversation
    # ------------------------------------

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.write(message["content"])

    # ------------------------------------
    # Chat Input
    # ------------------------------------

    question = st.chat_input(
        "Ask about stocks..."
    )

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question,
            }
        )

        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                answer = chat_with_ai(question)

            st.write(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        save_chat(
            st.session_state.user["id"],
            question,
            answer,
        )

    st.divider()

    # ------------------------------------
    # Quick Actions
    # ------------------------------------

    st.subheader("Quick Actions")

    c1, c2, c3 = st.columns(3)

    with c1:

        if st.button(
            "Analyze Stock",
            width="stretch",
        ):
            navigate("Stock Analysis")

    with c2:

        if st.button(
            "Financial Report",
            width="stretch",
        ):
            navigate("Report Analyzer")

    with c3:

        if st.button(
            "Market News",
            width="stretch",
        ):
            navigate("News & Sentiment")

    st.divider()

    st.caption(
        "© 2026 FinSight AI | AI-Powered Financial Research Platform"
    )