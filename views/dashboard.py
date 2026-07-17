import streamlit as st
import pandas as pd
import plotly.express as px


from data.companies import companies
from data.charts import get_chart_data


def show_dashboard():

    # ======================================================
# HERO SECTION
# ======================================================

    left, right = st.columns([4, 1])

    with left:

        st.markdown(
            """
            # 👋 Welcome to FinSight AI

            ### AI-powered Financial Research Platform

            Analyze stocks, discover market sentiment, generate AI insights,
            and make smarter investment decisions — all in one place.
            """
        )

    with right:

        st.metric(
            "🟢 Market Status",
            "OPEN"
        )

    st.write("")

    left, right = st.columns([5, 1])

    with left:

        company = st.text_input(
            "🔍 Search Company",
            value=st.session_state.get("company", "Apple"),
            placeholder="Search Apple, Tesla, NVIDIA..."
        )

        if company:
            st.session_state["company"] = company

    with right:

        st.write("")
        st.write("")

        if st.button(
            "Analyze",
             use_container_width=True,
             key="dashboard_analyze"
        ):
            st.success(f"Analyzing {company}...")

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

    cards = [
        ("📈", "NIFTY 50", "24,385", "+0.82%", "#16a34a"),
        ("🏦", "SENSEX", "80,642", "+0.65%", "#16a34a"),
        ("📄", "Reports", company_data["reports"], "Available", "#4F46E5"),
        ("🤖", "AI Accuracy", company_data["ai_accuracy"], "Trusted", "#F59E0B"),
    ]

    for col, (icon, title, value, subtitle, color) in zip(
        [c1, c2, c3, c4], cards
    ):

        with col:

            st.markdown(
                f"""
    <div class="kpi-card">

    <div class="kpi-top">
    <span class="kpi-icon">{icon}</span>
    <span class="kpi-title">{title}</span>
    </div>

    <div class="kpi-value">
    {value}
    </div>

    <div class="kpi-badge" style="background:{color};">
    {subtitle}
    </div>

    </div>
    """,
                unsafe_allow_html=True,
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
               markers=True,
               line_shape="spline"
            )

            fig.update_traces(
             line=dict(
              width=4,
              color="#4F46E5"
             ),
             marker=dict(
              size=8,
              color="#4F46E5",
              line=dict(
               width=2,
               color="white"
              )
            )
           )

            fig.update_layout(

             template="plotly_white",

             paper_bgcolor="rgba(0,0,0,0)",

             plot_bgcolor="white",

             margin=dict(
              l=15,
              r=15,
              t=20,
              b=15
             ),

             height=420,

             hovermode="x unified",

             xaxis_title="",

             yaxis_title="Stock Price ($)",

             font=dict(
              size=13,
              color="#374151"
             ),

             xaxis=dict(
              showgrid=False,
              zeroline=False
             ),

             yaxis=dict(
              gridcolor="#EEF2F7"
             ),

             legend=dict(
               orientation="h"
             )

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
             hole=.65,
             color_discrete_sequence=[
             "#4F46E5",
             "#10B981",
             "#F59E0B",
             "#EF4444",
             "#8B5CF6"
             ]
            )

            pie.update_layout(

             template="plotly_white",

             paper_bgcolor="rgba(0,0,0,0)",

             plot_bgcolor="rgba(0,0,0,0)",

             margin=dict(
              l=10,
              r=10,
              t=20,
              b=20
             ),

             font=dict(
              color="#374151",
              size=13
             ),

             height=420,

             legend=dict(
              orientation="h",
              y=-0.15
             )

           )
            
            pie.update_traces(
             textinfo="percent",
             textfont_size=14,
             marker=dict(
              line=dict(
               color="white",
               width=2
              )
             )
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
             ("🍎 Apple", "$189.42", "+2.4%"),
             ("🟢 NVIDIA", "$134.15", "+4.8%"),
             ("🚗 Tesla", "$252.61", "+1.6%"),
             ("🪟 Microsoft", "$442.18", "+2.1%")
            ]

            for name, price, change in stocks:

             st.markdown(
              f"""
            <div class="stock-card">

            <div class="stock-left">

            <div class="stock-name">{name}</div>

            <div class="stock-price">{price}</div>

            </div>

            <div class="stock-right">

            <span class="stock-change">{change}</span>

            </div>

            </div>
            """,
                unsafe_allow_html=True
               )

    with right:

        with st.container(border=True):

            st.subheader("📰 Latest Headlines")

            news = [

                  ("Apple expands AI investments.", "Technology", "2 min ago", "🟢 Bullish"),

                  ("NVIDIA reports record quarterly revenue.", "Earnings", "15 min ago", "🟢 Bullish"),

                  ("Tesla announces new Gigafactory.", "Automobile", "32 min ago", "🟡 Neutral"),

                  ("Microsoft launches new Copilot features.", "Artificial Intelligence", "1 hour ago", "🟢 Bullish"),

            ]

            for title, category, time, sentiment in news:

             color = "#DCFCE7" if "Bullish" in sentiment else "#FEF3C7"

             text = "#16A34A" if "Bullish" in sentiment else "#D97706"

             st.markdown(
              f"""
            <div class="news-card">

            <div class="news-title">
            {title}
            </div>

            <div class="news-footer">

            <span class="news-category">
            {category}
            </span>

            <span class="news-time">
            🕒 {time}
            </span>

            <span class="news-sentiment"
            style="background:{color};color:{text};">
            {sentiment}
            </span>

            </div>

            </div>
            """,
                unsafe_allow_html=True
                )

    st.write("")

    # ======================================================
    # AI INSIGHT
    # ======================================================

    with st.container(border=True):

        st.subheader("🤖 AI Investment Recommendation")

        st.markdown(
            """
    <div class="ai-card">

    <div class="ai-header">

    <div>

    <h3>🟢 BUY</h3>

    <p>Confidence Score: <b>92%</b></p>

    </div>

    <div class="confidence-circle">

    92%

    </div>

    </div>

    <hr>

    <h4>📈 Why the AI recommends BUY</h4>

    <ul>

    <li>Strong quarterly earnings growth.</li>

    <li>Positive news sentiment across financial media.</li>

    <li>Healthy technical indicators (RSI & MACD).</li>

    <li>Cloud and AI businesses continue expanding.</li>

    </ul>

    <h4>⚠ Risk Factors</h4>

    <ul>

    <li>Market volatility due to interest rates.</li>

    <li>Technology sector valuations remain elevated.</li>

    </ul>

    <p class="generated-time">
    Generated just now • FinSight AI Engine
    </p>

    </div>
    """,
            unsafe_allow_html=True,
        )

    st.write("")
    
    st.divider()

    st.caption("© 2026 FinSight AI | AI-Powered Financial Research Platform")