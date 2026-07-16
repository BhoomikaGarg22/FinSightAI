import streamlit as st


def metric_card(title, value, change=None, positive=True):
    """Reusable metric card"""

    with st.container(border=True):

        st.caption(title)

        st.markdown(f"## {value}")

        if change:

            if positive:
                st.success(change)
            else:
                st.error(change)
        else:
            st.write("")   # keeps all cards the same height

def section_title(title):
    st.markdown(f"## {title}")


def info_box(text):
    st.info(text)


def success_box(text):
    st.success(text)


def warning_box(text):
    st.warning(text)


def recommendation_card(recommendation, confidence):

    color = "🟢"

    if recommendation == "HOLD":
        color = "🟡"

    elif recommendation == "SELL":
        color = "🔴"

    st.success(f"""
### {color} {recommendation}

**Confidence:** {confidence}
""")


def loading_animation(text="Analyzing..."):
    return st.spinner(text)