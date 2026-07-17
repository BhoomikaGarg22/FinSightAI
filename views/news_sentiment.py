import streamlit as st
import pandas as pd
import plotly.express as px
import time
from data.companies import companies
def show_news_sentiment():

    # =====================================================
    # HEADER
    # =====================================================

    st.title("📰 AI News & Market Sentiment")
    st.caption(
        "Analyze the latest financial news and discover AI-powered market sentiment."
    )

    # =====================================================
# SEARCH
# =====================================================

    st.markdown("##### Search Company")

    col1, col2 = st.columns([6, 1], vertical_alignment="bottom")

    with col1:
        company = st.text_input(
            "",
            value=st.session_state.get("company", "Apple"),
            label_visibility="collapsed",
            placeholder="Enter company name..."
        )

        if company:
            st.session_state["company"] = company

    with col2:
        analyze = st.button(
            "🔍 Analyze",
            key="news_analyze",
            use_container_width=True
        )

    if analyze:
        with st.spinner("Analyzing latest news..."):
            time.sleep(2)

        st.success("News analysis complete!")

    st.write("")

    # =====================================================
    # SENTIMENT OVERVIEW
    # =====================================================

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.metric(
                "Overall Sentiment",
                "🟢 Bullish"
            )

    with c2:
        with st.container(border=True):
            st.metric(
                "Confidence",
                "91%"
            )

    with c3:
        with st.container(border=True):
            st.metric(
                "Articles Analyzed",
                "128"
            )

    st.write("")

    # =====================================================
    # NEWS + CHART
    # =====================================================

    left, right = st.columns([2, 1])

    with left:

        with st.container(border=True):

            st.subheader("📰 Latest Financial News")

            news = [
                (
                    "Apple unveils next-generation AI-powered Siri features.",
                    "CNBC • 2 hours ago"
                ),
                (
                    "NVIDIA becomes one of the world's most valuable companies.",
                    "Bloomberg • 5 hours ago"
                ),
                (
                    "Tesla expands autonomous vehicle rollout in Europe.",
                    "Reuters • Today"
                ),
                (
                    "Microsoft strengthens enterprise AI partnerships.",
                    "Financial Times • Today"
                ),
            ]

            for headline, source in news:

                st.markdown(f"**{headline}**")
                st.caption(source)
                st.divider()

    with right:

        with st.container(border=True):

            st.subheader("📈 Sentiment Trend")

            df = pd.DataFrame({
                "Day": [
                    "Mon",
                    "Tue",
                    "Wed",
                    "Thu",
                    "Fri"
                ],
                "Score": [
                    70,
                    75,
                    81,
                    87,
                    91
                ]
            })

            fig = px.line(
                df,
                x="Day",
                y="Score",
                markers=True
            )

            fig.update_layout(
                height=350,
                margin=dict(
                    l=10,
                    r=10,
                    t=20,
                    b=10
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    st.write("")

    # =====================================================
    # AI SUMMARY
    # =====================================================

    with st.container(border=True):

        st.subheader("🤖 AI Summary")

        st.success("""
### Market Outlook

Technology stocks continue to dominate market headlines.

Positive earnings, rapid AI adoption and cloud expansion
are supporting strong investor confidence.

Overall outlook remains **Bullish**.
""")

    st.write("")

    # =====================================================
    # POSITIVE VS NEGATIVE
    # =====================================================

    left, right = st.columns(2)

    with left:

        with st.container(border=True):

            st.subheader("✅ Positive Factors")

            st.markdown("""
- Strong quarterly earnings

- AI product launches

- Analyst upgrades

- Institutional buying

- Cloud growth
""")

    with right:

        with st.container(border=True):

            st.subheader("⚠ Risks")

            st.markdown("""
- High market valuation

- Global uncertainty

- Competition

- Regulatory pressure

- Inflation concerns
""")

    st.write("")

    # =====================================================
    # QUICK ACTIONS
    # =====================================================

    with st.container(border=True):

        st.subheader("⚡ Quick Actions")

        b1, b2, b3 = st.columns(3)

        with b1:
            st.button(
                "📊 View Stock",
                key="view_stock",
                use_container_width=True
            )

        with b2:
            st.button(
                "🤖 Ask AI",
                key="news_ai",
                use_container_width=True
            )

        with b3:
            if st.button("Analyze"):
             with st.spinner("Analyzing news"):
              
              time.sleep(2)

    st.success("Analysis Complete!")

    st.divider()

    st.caption(
        "© 2026 FinSight AI | AI-Powered Financial Research Platform"
    )