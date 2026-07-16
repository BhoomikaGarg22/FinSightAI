import streamlit as st


def show_sidebar():

    with st.sidebar:

        #st.image("assets/logo.png", width=90)

        st.markdown("""
# 💹 FinSight AI

##### AI-Powered Financial Research
""")

        st.divider()

        page = st.radio(
            "",
            [
                "🏠 Dashboard",
                "📈 Stock Analysis",
                "📄 Report Analyzer",
                "📰 News & Sentiment",
                "🤖 AI Chat",
                "⚙️ Settings",
            ],
            label_visibility="collapsed",
        )

        st.divider()

        st.caption("Version 1.0")
        st.caption("Made with ❤️ using Streamlit")

    return page.replace("🏠 ", "").replace("📈 ", "").replace("📄 ", "").replace("📰 ", "").replace("🤖 ", "").replace("⚙️ ", "")