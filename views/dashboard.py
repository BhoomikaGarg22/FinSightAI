import streamlit as st
import pandas as pd
import plotly.express as px


from data.companies import companies
from data.charts import get_chart_data


def show_dashboard():

    st.info("🧪 Demo Mode • Using sample financial data. Live AI integration in progress.")

    # HEADER
    st.title("💹 FinSight AI Dashboard")
    st.caption("AI-powered financial research and investment insights.")

    company = st.text_input(
        "Search Company",
        value=st.session_state.get("company", "Apple")
)

    if company:
     st.session_state["company"] = company

    company = st.session_state.get("company", "Apple")

    company_data = companies.get(
        company,
        companies["Apple"]
)
    st.write("")

    # ======================================================
    # KPI CARDS
    # ======================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        with st.container(border=True):
            st.metric("📈 NIFTY 50", "24,385", "+0.82%")

    with c2:
        with st.container(border=True):
            st.metric("🏦 SENSEX", "80,642", "+0.65%")

    with c3:
        with st.container(border=True):
            st.metric("📄 Reports", company_data["reports"]
        )
    with c4:
        with st.container(border=True):
            st.metric("🤖 AI Accuracy",company_data["ai_accuracy"]
        )

    st.write("")

    # ======================================================
    # CHARTS
    # ======================================================

    left, right = st.columns([2, 1])

    with left:

        with st.container(border=True):

            st.subheader("📈 Market Overview")

            df = get_chart_data(company)

            fig = px.line(
                df,
                x="Date",
                y="Price",
                markers=True
            )

            fig.update_layout(
             template="plotly_dark",
             paper_bgcolor="rgba(0,0,0,0)",
             plot_bgcolor="rgba(0,0,0,0)",
             font=dict(color="#F8FAFC"),
             margin=dict(l=20, r=20, t=20, b=20),
             height=420,
            )

            st.plotly_chart(fig, use_container_width=True)

    with right:

        with st.container(border=True):

            st.subheader("📊 Sector Allocation")

            sector_df = pd.DataFrame({
                "Sector": [
                    "Technology",
                    "Finance",
                    "Healthcare",
                    "Energy",
                    "Others"
                ],
                "Allocation": [
                    38,
                    22,
                    18,
                    12,
                    10
                ]
            })

            pie = px.pie(
                sector_df,
                names="Sector",
                values="Allocation",
                hole=0.45
            )

            pie.update_layout(
             template="plotly_dark",
             paper_bgcolor="rgba(0,0,0,0)",
             plot_bgcolor="rgba(0,0,0,0)",
             font=dict(color="#F8FAFC"),
             height=420,
            )

            st.plotly_chart(
                pie,
                use_container_width=True
            )

    st.write("")

    # ======================================================
    # TRENDING + NEWS
    # ======================================================

    left, right = st.columns(2)

    with left:

        with st.container(border=True):

            st.subheader("🔥 Trending Stocks")

            stocks = [
                ("Apple", "$189.42", "+2.4%"),
                ("NVIDIA", "$134.15", "+4.8%"),
                ("Tesla", "$252.61", "+1.6%"),
                ("Microsoft", "$442.18", "+2.1%")
            ]

            for name, price, change in stocks:
                st.markdown(
                    f"**{name}** &nbsp;&nbsp; {price} &nbsp;&nbsp; 🟢 {change}"
                )

    with right:

        with st.container(border=True):

            st.subheader("📰 Latest Headlines")

            st.info("Apple expands AI investments.")
            st.info("NVIDIA reports record quarterly revenue.")
            st.info("Tesla announces new Gigafactory.")
            st.info("Microsoft launches new Copilot features.")

    st.write("")

    # ======================================================
    # AI INSIGHT
    # ======================================================

    with st.container(border=True):

        st.subheader("🤖 Today's AI Insight")

        st.success(
            """
Technology stocks continue showing strong momentum.

✅ AI adoption is accelerating.

✅ Investor sentiment remains positive.

✅ Cloud and semiconductor sectors are expected to outperform.

**Overall Recommendation: BUY**

Confidence Score: **92%**
"""
    )

    st.write("")
    
    st.divider()

    st.caption("© 2026 FinSight AI | AI-Powered Financial Research Platform")