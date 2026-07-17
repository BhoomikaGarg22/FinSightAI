import streamlit as st

def navigate(page, company=None):
    st.session_state.page = page

    if company:
        st.session_state.company = company

    st.rerun()