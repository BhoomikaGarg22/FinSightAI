import streamlit as st


def show_settings():

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown("""
    <div class="page-header">

    <h1>Settings</h1>

    <p>
    Manage your profile, preferences, notifications,
    and personalize your FinSight AI experience.
    </p>

    <div class="market-status">

    <span class="status-dot"></span>

    <b>Preferences Saved</b>

    </div>

    </div>
    """, unsafe_allow_html=True)
    st.write("")

    # =====================================================
    # PROFILE
    # =====================================================

    with st.container(border=True):

        st.subheader("Profile")
        st.caption("Update your personal information.")
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

        st.subheader("Appearance")
        st.caption(
         "Customize how FinSight AI looks and behaves."
        )
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

        st.subheader("Notifications")

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
    
    with st.container(border=True):

        st.subheader("Account")

        st.selectbox(
            "Language",
            [
                "English",
                "Hindi"
            ]
        )

        st.selectbox(
            "Currency",
            [
                "USD",
                "INR"
            ]
        )
    st.write("")
    
    with st.container(border=True):

        st.subheader("Privacy")

        st.toggle(
            "Share anonymous analytics",
            value=False
        )

        st.toggle(
            "Remember recent searches",
            value=True
        )
    # =====================================================
    # ACTIONS
    # =====================================================

    with st.container(border=True):

        st.subheader("Actions")

        b1, b2, b3 = st.columns(3)

        with b1:
         if st.button(
          "Save Settings",
          use_container_width=True
        ):
            st.success("Settings saved successfully!")

        with b2:
         if st.button(
          "Reset",
          use_container_width=True
        ):
            st.rerun()

        with b3:
         if st.button(
          "Logout",
          use_container_width=True
        ):
            st.session_state.clear()
            st.rerun()

    st.divider()

    st.caption("FinSight AI • Version 1.0.0 • Demo Environment")