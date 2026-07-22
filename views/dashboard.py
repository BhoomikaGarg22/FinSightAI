import base64
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.navigation import navigate
from data.companies import companies
import yfinance as yf

def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()


COMPANY_LOGO_MAP = {
    "Apple": "assets/images/apple_logo.png",
    "Tesla": "assets/images/Tesla_Logo.png",
    "NVIDIA": "assets/images/Nvidia_Logo.png",
    "Microsoft": "assets/images/Microsoft_Logo.png",
}
def get_stock_history(ticker):
    try:
        df = yf.download(
            ticker,
            period="6mo",
            interval="1d",
            progress=False
        )
        if df.empty:
            return None
        df = df.reset_index()
        df = df[["Date", "Close"]]

        df.columns = ["Date", "Price"]

        return df

    except Exception as e:
        print(e)
        return None

COMPANY_TICKERS = {
    "Apple": "AAPL",
    "Tesla": "TSLA",
    "Microsoft": "MSFT",
    "NVIDIA": "NVDA"
}


def show_dashboard():

    # ======================================================
# HERO SECTION
# ======================================================

    left, right = st.columns([4, 1])

    with left:

        logo_b64 = get_base64_image("assets/images/icon_logo.png")

        st.markdown(
            f"""
            <div style="display:flex; align-items:center; gap:12px; margin-bottom: 0.25rem;">
                <img src="data:image/png;base64,{logo_b64}" style="width:72px; height:auto; object-fit:contain;">
                <h1 style="margin: 0;">Welcome to FinSight AI</h1>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            ### AI-powered Financial Research Platform

            Analyze stocks, discover market sentiment, generate AI insights,
            and make smarter investment decisions — all in one place.
            """
        )

    with right:

        st.markdown(
            "<div style='margin-top: 2.5rem;'></div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <style>
            .market-status-card {
                background: linear-gradient(135deg, #16a34a, #22c55e);
                color: white;
                border-radius: 14px;
                padding: 14px 16px;
                text-align: center;
                box-shadow: 0 8px 24px rgba(22, 162, 74, 0.28);
                animation: pulseGreen 1.6s infinite;
                margin-top: 6px;
            }
            .market-status-title {
                font-size: 13px;
                font-weight: 600;
                letter-spacing: 0.3px;
                opacity: 0.9;
            }
            .market-status-value {
                font-size: 24px;
                font-weight: 800;
                margin-top: 6px;
            }
            @keyframes pulseGreen {
                0% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.55); }
                70% { box-shadow: 0 0 0 10px rgba(34, 197, 94, 0.0); }
                100% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.0); }
            }
            </style>
            <div class="market-status-card">
                <div class="market-status-title">Market Status</div>
                <div class="market-status-value">OPEN</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    left, right = st.columns([5, 1])

    with left:

        from utils.helpers import render_company_selector
        company = render_company_selector("Search Company")

    with right:

        st.write("")
        st.write("")

        if st.button(
            "Analyze",
             use_container_width=True,
        ):
            if company:
                navigate("Stock Analysis")
                st.success(f"Analyzing {company}...")
            else:
                st.warning("Please select a company first.")


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

            st.subheader("Market Overview")

            fig = go.Figure()

            colors = {
                "Apple": "#4F46E5",
                "Tesla": "#EF4444",
                "Microsoft": "#10B981",
                "NVIDIA": "#F59E0B",
            }

            for name, ticker in COMPANY_TICKERS.items():

                df = get_stock_history(ticker)

                if df is None or df.empty:
                    continue

                fig.add_trace(
                    go.Scatter(
                        x=df["Date"],
                        y=df["Price"],
                        mode="lines",
                        name=name,
                        line=dict(
                            width=3,
                            color=colors[name]
                        )
                    )
                )

            fig.update_layout(

                template="plotly_white",

                height=500,

                hovermode="x unified",

                paper_bgcolor="white",

                plot_bgcolor="white",

                margin=dict(
                    l=20,
                    r=20,
                    t=20,
                    b=20
                ),

                xaxis=dict(
                    title="Date",
                    showgrid=False
                ),

                yaxis=dict(
                    title="Stock Price ($)",
                    showgrid=True,
                    gridcolor="#ECECEC"
                ),

                legend=dict(
                    orientation="h",
                    y=1.05,
                    x=0
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    with right:

        with st.container(border=True):

            st.subheader("Sector Allocation")

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
                hole=0.65,
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

                height=500,

                paper_bgcolor="rgba(0,0,0,0)",

                plot_bgcolor="rgba(0,0,0,0)",

                margin=dict(
                    l=10,
                    r=10,
                    t=20,
                    b=20
                ),

                showlegend=True,

                legend=dict(
                    orientation="v",
                    x=1,
                    xanchor="left",
                    y=0.5,
                    yanchor="middle",
                    font=dict(
                        size=13,
                        color="#111827"
                    )
                ),

                font=dict(
                    color="#111827"
                )
            )

            pie.update_traces(
                textinfo="percent",
                textfont_size=13,
                marker=dict(
                    line=dict(
                        color="white",
                        width=2
                    )
                ),
                hovertemplate="<b>%{label}</b><br>%{value}%<extra></extra>"
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

            st.subheader("Trending Stocks")

            stocks = [
             ("Apple", "$189.42", "+2.4%"),
             ("NVIDIA", "$134.15", "+4.8%"),
             ("Tesla", "$252.61", "+1.6%"),
             ("Microsoft", "$442.18", "+2.1%")
            ]

            for name, price, change in stocks:

             logo_path = COMPANY_LOGO_MAP.get(name, "assets/images/icon_logo.png")
             logo_b64 = get_base64_image(logo_path)

             st.markdown(
              f"""
            <div class="stock-card">

            <div class="stock-left" style="display:flex; align-items:center; gap:12px;">

            <img src="data:image/png;base64,{logo_b64}" style="width:34px; height:34px; object-fit:contain; border-radius:8px;">

            <div>
                <div class="stock-name">{name}</div>
                <div class="stock-price">{price}</div>
            </div>

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

            st.subheader("Latest Headlines")

            news = [

                  ("Apple expands AI investments.", "Technology", "2 min ago", "Bullish"),

                  ("NVIDIA reports record quarterly revenue.", "Earnings", "15 min ago", "Bullish"),

                  ("Tesla announces new Gigafactory.", "Automobile", "32 min ago", "Neutral"),

                  ("Microsoft launches new Copilot features.", "Artificial Intelligence", "1 hour ago", "Bullish"),

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
             {time}
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

        st.subheader("AI Investment Recommendation")

        st.markdown(
            """
    <div class="ai-card">

    <div class="ai-header">

    <div>

    <h3>BUY</h3>

    <p>Confidence Score: <b>92%</b></p>

    </div>

    <div class="confidence-circle">

    92%

    </div>

    </div>

    <hr>

    <h4>Why the AI recommends BUY</h4>

    <ul>

    <li>Strong quarterly earnings growth.</li>

    <li>Positive news sentiment across financial media.</li>

    <li>Healthy technical indicators (RSI & MACD).</li>

    <li>Cloud and AI businesses continue expanding.</li>

    </ul>

    <h4>Risk Factors</h4>

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