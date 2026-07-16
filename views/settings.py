import streamlit as st


def show_settings():

    # =====================================================
    # HEADER
    # =====================================================

    st.title("⚙️ Settings")
    st.caption("Customize your FinSight AI experience.")

    st.write("")

    # =====================================================
    # PROFILE
    # =====================================================

    with st.container(border=True):

        st.subheader("👤 Profile")

        c1, c2 = st.columns(2)

        with c1:
            st.text_input(
                "Name",
                value="Demo User"
            )

        with c2:
            st.text_input(
                "Email",
                value="demo@finsight.ai"
            )

    st.write("")

    # =====================================================
    # APPEARANCE
    # =====================================================

    with st.container(border=True):

        st.subheader("🎨 Appearance")

        st.selectbox(
            "Theme",
            [
                "System Default",
                "Light",
                "Dark"
            ]
        )

        st.checkbox(
            "Compact Dashboard",
            value=True
        )

    st.write("")

    # =====================================================
    # NOTIFICATIONS
    # =====================================================

    with st.container(border=True):

        st.subheader("🔔 Notifications")

        st.toggle(
            "Daily Market Summary",
            value=True
        )

        st.toggle(
            "Breaking Financial News",
            value=True
        )

        st.toggle(
            "AI Investment Alerts",
            value=False
        )

    st.write("")

    # =====================================================
    # API STATUS
    # =====================================================

    with st.container(border=True):

        st.subheader("🔌 Connected Services")

        c1, c2 = st.columns(2)

        with c1:
            st.success("✅ Gemini API")

        with c2:
            st.success("✅ Financial News API")

        c3, c4 = st.columns(2)

        with c3:
            st.success("✅ Stock Market API")

        with c4:
            st.info("⏳ Database Connection")

    st.write("")

    # =====================================================
    # ABOUT
    # =====================================================

    with st.container(border=True):

        st.subheader("ℹ️ About FinSight AI")

        st.markdown("""
**Version:** 1.0

**Developed for:** Hackathon 2026

**Technology Stack**

- Streamlit
- Python
- Plotly
- Gemini AI
- Financial APIs

FinSight AI is an AI-powered financial research assistant
that helps investors analyze stocks, company reports,
market news and financial sentiment.
""")

    st.write("")

    # =====================================================
    # ACTIONS
    # =====================================================

    with st.container(border=True):

        st.subheader("⚡ Actions")

        b1, b2, b3 = st.columns(3)

        with b1:
            st.button(
                "💾 Save Settings",
                key="save_settings",
                use_container_width=True
            )

        with b2:
            st.button(
                "🔄 Reset",
                key="reset_settings",
                use_container_width=True
            )

        with b3:
            st.button(
                "🚪 Logout",
                key="logout",
                use_container_width=True
            )

    st.divider()

    st.caption("© 2026 FinSight AI | AI-Powered Financial Research Platform")