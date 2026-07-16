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

import streamlit as st

def action_button(label, key=None, button_type="primary", use_container_width=True):
    """
    button_type:
    primary  -> Indigo
    success  -> Green
    warning  -> Amber
    danger   -> Red
    """

    st.markdown(
        f"""
        <style>
        div.stButton button[data-testid="{key}"] {{
            border-radius:12px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    return st.button(
        label,
        key=key,
        type=button_type,
        use_container_width=use_container_width,
    )

import streamlit as st


def primary_button(label, key=None, use_container_width=True):
    return st.button(
        label,
        key=key,
        type="primary",
        use_container_width=use_container_width,
    )


def secondary_button(label, key=None, use_container_width=True):
    return st.button(
        label,
        key=key,
        use_container_width=use_container_width,
    )