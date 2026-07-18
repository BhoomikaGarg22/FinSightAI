import streamlit as st
import base64


def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()


def show_sidebar():

    with st.sidebar:

        logo = get_base64_image("assets/images/Whitebg_logo.png")

        st.markdown(
            f"""
            <div style="
                display:flex;
                justify-content:center;
                margin-top:-8px;
                margin-bottom:2px;
            ">
                <img
                    src="data:image/png;base64,{logo}"
                    style="width:250px;height:auto;">
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            "<hr style='margin:12px 0 10px 0;'>",
            unsafe_allow_html=True,
        )

        pages = [
            "Dashboard",
            "Stock Analysis",
            "Watchlist",
            "Report Analyzer",
            "News & Sentiment",
            "AI Chat",
            "Settings",
        ]

        if "current_page" not in st.session_state:
            st.session_state.current_page = "Dashboard"

        selected = st.radio(
            "",
            pages,
            index=pages.index(st.session_state.current_page),
            label_visibility="collapsed",
        )


    # User clicked sidebar
        if selected != st.session_state.current_page:
            st.session_state.current_page = selected
            st.rerun()

        return st.session_state.current_page