import streamlit as st
import base64


# -------------------------------------------------------
# Helper
# -------------------------------------------------------

def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()


# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

def show_sidebar():

    with st.sidebar:

        # ==========================================
        # Logo
        # ==========================================

        logo = get_base64_image(
            "assets/images/Whitebg_logo.png"
        )

        st.markdown(
            f"""
<div style="
display:flex;
justify-content:center;
margin-top:8px;
margin-bottom:12px;
">
<img
src="data:image/png;base64,{logo}"
style="width:215px;">
</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown("<hr>", unsafe_allow_html=True)

        # ==========================================
        # User
        # ==========================================

        if st.session_state.get("user"):

            user = st.session_state.user

            profile = user.get("profile", {})

            role = profile.get(
                "investor_type",
                "Investor",
            )

            display_name = (
                profile.get("display_name")
                or user.get("email", "User").split("@")[0]
            )

            st.markdown(
                f"""
<div style="padding:4px 6px 16px 6px;">

<div style="
font-size:22px;
font-weight:700;
color:#111827;
line-height:1.2;
">
{display_name}
</div>

<div style="
font-size:14px;
color:#64748B;
margin-top:4px;
">
{role}
</div>

</div>
""",
                unsafe_allow_html=True,
            )

        st.markdown("<hr>", unsafe_allow_html=True)

        # ==========================================
        # Navigation
        # ==========================================

        pages = [
            "🏠 Dashboard",
            "📈 Stock Analysis",
            "⭐ Watchlist",
            "📄 Report Analyzer",
            "📰 News & Sentiment",
            "🤖 AI Chat",
            "⚙️ Settings",
        ]

        mapping = {
            "🏠 Dashboard": "Dashboard",
            "📈 Stock Analysis": "Stock Analysis",
            "⭐ Watchlist": "Watchlist",
            "📄 Report Analyzer": "Report Analyzer",
            "📰 News & Sentiment": "News & Sentiment",
            "🤖 AI Chat": "AI Chat",
            "⚙️ Settings": "Settings",
        }

        reverse = {v: k for k, v in mapping.items()}

        if "current_page" not in st.session_state:
            st.session_state.current_page = "Dashboard"

        selected = st.radio(
            "Navigation",
            pages,
            index=pages.index(
                reverse[st.session_state.current_page]
            ),
            label_visibility="collapsed",
        )

        if mapping[selected] != st.session_state.current_page:
            st.session_state.current_page = mapping[selected]
            st.rerun()

        st.markdown("<hr>", unsafe_allow_html=True)

        # ==========================================
        # Logout
        # ==========================================

        if st.button(
            "🚪 Logout",
            use_container_width=True,
        ):

            st.session_state.logged_in = False
            st.session_state.user = None

            if "profile" in st.session_state:
                del st.session_state.profile

            st.session_state.current_page = "Dashboard"

            if "messages" in st.session_state:
                del st.session_state.messages

            st.rerun()

        st.markdown("<hr>", unsafe_allow_html=True)

        # ==========================================
        # Footer
        # ==========================================

        st.markdown(
            """
<div style="
text-align:center;
font-size:12px;
color:#94A3B8;
padding-bottom:8px;
">

<b>FinSight AI</b><br>

Version 1.0

</div>
""",
            unsafe_allow_html=True,
        )

    return st.session_state.current_page