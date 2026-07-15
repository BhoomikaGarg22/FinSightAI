import streamlit as st
import pandas as pd
import plotly.express as px


def show_dashboard():

    st.title("Welcome to FinSight AI")

    st.markdown(
        "Your AI-powered assistant for smarter financial research and investment insights."
    )

    company = st.text_input(
        "Search Company",
        placeholder="Apple, Tesla, NVIDIA..."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Live Stock Price",
            "$189.42",
            "+2.14%"
        )

    with col2:
        st.metric(
            "Market Sentiment",
            "Bullish",
            "+8.6%"
        )

    col3, col4 = st.columns(2)

    with col3:
        st.metric(
            "Reports Analyzed",
            "1284",
            "+124"
        )

    with col4:
        st.metric(
            "AI Queries Today",
            "3942",
            "-1.2%"
        )

    df = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
        "Price": [182, 184, 183, 188, 189]
    })

    fig = px.line(df, x="Day", y="Price")

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Latest Financial News")

    st.info("Apple launches new AI-powered services.")
    st.info("Tesla shares gain after strong quarterly earnings.")
    st.info("NVIDIA announces next-generation AI chips.")

    st.subheader("AI Summary")

    st.success("""
Overall market sentiment appears bullish.

Technology stocks continue showing strong momentum driven by AI innovation and positive earnings.
""")

    st.subheader("Quick Actions")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.button("Analyze Stock")

    with c2:
        st.button("Upload Report")

    with c3:
        st.button("Ask AI") 