import streamlit as st

def navigate(page, **kwargs):
    st.session_state.current_page = page

    for key, value in kwargs.items():
        st.session_state[key] = value

    st.rerun()