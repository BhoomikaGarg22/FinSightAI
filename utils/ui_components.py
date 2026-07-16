import streamlit as st


def metric_card(title, value, change, positive=True):
    delta_color = "normal" if positive else "inverse"

    with st.container(border=True):

     st.caption("Current Price")

    st.markdown("# $189.42")

    st.success("+2.14% Today")


def section_title(title):
    st.markdown(f"## {title}")


def info_box(text):
    st.info(text)


def success_box(text):
    st.success(text)