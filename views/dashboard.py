import base64

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.navigation import navigate
from utils.helpers import (
    render_company_selector,
    get_selected_company,
)

from data.companies import companies
from data.stock_history import get_stock_history


def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()


COMPANY_LOGO_MAP = {
    "Apple": "assets/images/apple_logo.png",
    "Tesla": "assets/images/Tesla_Logo.png",
    "NVIDIA": "assets/images/Nvidia_Logo.png",
    "Microsoft": "assets/images/Microsoft_Logo.png",
}


COMPANY_TICKERS = {
    "Apple": "AAPL",
    "Tesla": "TSLA",
    "Microsoft": "MSFT",
    "NVIDIA": "NVDA",
}


def show_dashboard():

    # ======================================================
    # HERO SECTION
    # ======================================================

    hero_left, hero_right = st.columns([4, 1])

    with hero_left:

        logo_b64 = get_base64_image(
            "assets/images/icon_logo.png"
        )

        st.markdown(
            f"""
            <div style="display:flex;align-items:center;gap:14px;margin-bottom:8px;">
                <img src="data:image/png;base64,{logo_b64}"
                     style="width:72px;height:72px;object-fit:contain;">

                <div>

                    <h1 style="margin:0;">
                        Welcome to FinSight AI
                    </h1>

                    <p style="
                        margin:4px 0 0;
                        color:#6B7280;
                        font-size:18px;
                    ">
                        AI-powered Financial Research Platform
                    </p>

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
Analyze stocks, discover financial news,
understand market sentiment,
generate AI-powered investment insights,
and make smarter investment decisions —
all from one modern dashboard.
"""
        )

    with hero_right:

        st.markdown(
            "<div style='margin-top:40px'></div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            """
<style>

.market-status-card{

background:linear-gradient(135deg,#16a34a,#22c55e);

border-radius:18px;

padding:18px;

color:white;

text-align:center;

box-shadow:0 10px 28px rgba(34,197,94,.25);

animation:pulseGreen 1.8s infinite;

}

.market-status-title{

font-size:13px;

font-weight:600;

opacity:.9;

letter-spacing:.4px;

}

.market-status-value{

margin-top:8px;

font-size:24px;

font-weight:800;

}

@keyframes pulseGreen{

0%{
box-shadow:0 0 0 0 rgba(34,197,94,.45);
}

70%{
box-shadow:0 0 0 12px rgba(34,197,94,0);
}

100%{
box-shadow:0 0 0 0 rgba(34,197,94,0);
}

}

</style>

<div class="market-status-card">

<div class="market-status-title">

Market Status

</div>

<div class="market-status-value">

OPEN

</div>

</div>
""",
            unsafe_allow_html=True,
        )

    st.write("")

    # ======================================================
    # COMPANY SEARCH
    # ======================================================

    left, right = st.columns([5, 1])

    with left:

        render_company_selector("Search Company")

        company = get_selected_company()

        if company is None:
            company = "Apple"

    with right:

        st.write("")
        st.write("")

        if st.button(
            "Analyze",
            use_container_width=True,
        ):

            navigate(
                "Stock Analysis",
                company=company,
            )

    company_data = companies.get(
        company,
        companies["Apple"],
    )

    st.write("")

    # ======================================================
    # KPI CARDS
    # ======================================================

    c1, c2, c3, c4 = st.columns(4)

    cards = [

        ("📈", "NIFTY 50", "24,385", "+0.82%", "#16A34A"),

        ("🏦", "SENSEX", "80,642", "+0.65%", "#16A34A"),

        (
            "📄",
            "Reports",
            company_data["reports"],
            "Available",
            "#4F46E5",
        ),

        (
            "🤖",
            "AI Accuracy",
            company_data["ai_accuracy"],
            "Trusted",
            "#F59E0B",
        ),

    ]

    for col, (icon, title, value, badge, color) in zip(
        [c1, c2, c3, c4],
        cards,
    ):

        with col:

            st.markdown(
                f"""
<div class="kpi-card">

<div class="kpi-top">

<span class="kpi-icon">

{icon}

</span>

<span class="kpi-title">

{title}

</span>

</div>

<div class="kpi-value">

{value}

</div>

<div
class="kpi-badge"
style="background:{color};"
>

{badge}

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

    # ======================================================
    # MARKET OVERVIEW
    # ======================================================

    with left:

        with st.container(border=True):

            st.subheader("Market Overview")

            # Selected company graph
            if company:

                ticker = COMPANY_TICKERS.get(company, "AAPL")

                df = get_stock_history(ticker)

                if df is None:

                    st.error("Unable to fetch stock data.")

                else:

                    fig = px.line(
                        df,
                        x="Date",
                        y="Price",
                        markers=True,
                    )

                    fig.update_traces(
                        line=dict(
                            color="#4F46E5",
                            width=4,
                            shape="spline",
                        ),
                        marker=dict(
                            size=7,
                            color="#4F46E5",
                            line=dict(
                                color="white",
                                width=2,
                            ),
                        ),
                        hovertemplate="<b>%{x}</b><br>$%{y:.2f}<extra></extra>",
                    )

            else:

                fig = go.Figure()

                colors = {
                    "Apple": "#4F46E5",
                    "Tesla": "#EF4444",
                    "Microsoft": "#10B981",
                    "NVIDIA": "#F59E0B",
                }

                for stock_name, ticker in COMPANY_TICKERS.items():

                    stock_df = get_stock_history(ticker)

                    if stock_df is None:
                        continue

                    fig.add_trace(
                        go.Scatter(
                            x=stock_df["Date"],
                            y=stock_df["Price"],
                            mode="lines",
                            name=stock_name,
                            line=dict(
                                width=3,
                                color=colors[stock_name],
                            ),
                        )
                    )

            fig.update_layout(

                template="plotly_white",

                paper_bgcolor="rgba(0,0,0,0)",

                plot_bgcolor="white",

                height=430,

                margin=dict(
                    l=15,
                    r=15,
                    t=20,
                    b=15,
                ),

                hovermode="x unified",

                font=dict(
                    family="Inter",
                    size=13,
                    color="#374151",
                ),

                xaxis=dict(
                    title="",
                    showgrid=False,
                    zeroline=False,
                    showline=True,
                    linecolor="#E5E7EB",
                ),

                yaxis=dict(
                    title="Stock Price ($)",
                    gridcolor="#EEF2F7",
                    zeroline=False,
                ),

                legend=dict(
                    orientation="h",
                    y=1.02,
                    x=0.5,
                    xanchor="center",
                    font=dict(
                        size=12,
                        color="#374151",
                    ),
                ),
            )

            st.plotly_chart(
                fig,
                use_container_width=True,
                config={
                    "displayModeBar": False,
                    "responsive": True,
                },
            )

    # ======================================================
    # SECTOR ALLOCATION
    # ======================================================

    with right:

        with st.container(border=True):

            st.subheader("Sector Allocation")

            sector_df = pd.DataFrame({

                "Sector": [
                    "Technology",
                    "Finance",
                    "Healthcare",
                    "Energy",
                    "Others",
                ],

                "Allocation": [
                    38,
                    22,
                    18,
                    12,
                    10,
                ],
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
                    "#8B5CF6",
                ],
            )

            pie.update_traces(

                textinfo="percent",

                textfont_size=14,

                textfont_color="white",

                marker=dict(
                    line=dict(
                        color="white",
                        width=2,
                    ),
                ),

                hovertemplate="%{label}<br>%{value}%<extra></extra>",
            )

            pie.update_layout(

                template="plotly_white",

                paper_bgcolor="rgba(0,0,0,0)",

                plot_bgcolor="rgba(0,0,0,0)",

                height=430,

                margin=dict(
                    l=10,
                    r=10,
                    t=20,
                    b=20,
                ),

                font=dict(
                    family="Inter",
                    size=13,
                    color="#374151",
                ),

                legend=dict(
                    orientation="h",
                    y=-0.18,
                    x=0.5,
                    xanchor="center",
                    font=dict(
                        color="#374151",
                        size=12,
                    ),
                ),
            )

            st.plotly_chart(
                pie,
                use_container_width=True,
                config={
                    "displayModeBar": False,
                },
            )

    st.write("")

        # ======================================================
    # TRENDING + NEWS
    # ======================================================

    left, right = st.columns(2)

    # ======================================================
    # TRENDING STOCKS
    # ======================================================

    with left:

        with st.container(border=True):

            st.subheader("Trending Stocks")

            stocks = [
                ("Apple", "$189.42", "+2.4%"),
                ("NVIDIA", "$134.15", "+4.8%"),
                ("Tesla", "$252.61", "+1.6%"),
                ("Microsoft", "$442.18", "+2.1%"),
            ]

            for name, price, change in stocks:

                logo_path = COMPANY_LOGO_MAP.get(
                    name,
                    "assets/images/icon_logo.png",
                )

                logo_b64 = get_base64_image(logo_path)

                st.markdown(
                    f"""
<div style="
display:flex;
justify-content:space-between;
align-items:center;
padding:14px 16px;
margin-bottom:12px;
border:1px solid #E5E7EB;
border-radius:16px;
background:white;
box-shadow:0 2px 10px rgba(0,0,0,.05);
">

<div style="
display:flex;
align-items:center;
gap:12px;
">

<img
src="data:image/png;base64,{logo_b64}"
style="
width:36px;
height:36px;
object-fit:contain;
border-radius:8px;
">

<div>

<div style="
font-size:15px;
font-weight:600;
color:#111827;
">

{name}

</div>

<div style="
font-size:13px;
color:#6B7280;
">

{price}

</div>

</div>

</div>

<div style="
font-size:14px;
font-weight:700;
color:#16A34A;
">

{change}

</div>

</div>
""",
                    unsafe_allow_html=True,
                )

    # ======================================================
    # LATEST NEWS
    # ======================================================

    with right:

        with st.container(border=True):

            st.subheader("Latest Headlines")

            news = [

                (
                    "Apple expands AI investments.",
                    "Technology",
                    "2 min ago",
                    "Bullish",
                ),

                (
                    "NVIDIA reports record quarterly revenue.",
                    "Earnings",
                    "15 min ago",
                    "Bullish",
                ),

                (
                    "Tesla announces new Gigafactory.",
                    "Automobile",
                    "32 min ago",
                    "Neutral",
                ),

                (
                    "Microsoft launches new Copilot features.",
                    "Artificial Intelligence",
                    "1 hour ago",
                    "Bullish",
                ),

            ]

            for title, category, time, sentiment in news:

                badge_bg = (
                    "#DCFCE7"
                    if sentiment == "Bullish"
                    else "#FEF3C7"
                )

                badge_text = (
                    "#16A34A"
                    if sentiment == "Bullish"
                    else "#D97706"
                )

                st.markdown(
                    f"""
<div style="
padding:16px;
margin-bottom:14px;
border:1px solid #E5E7EB;
border-radius:16px;
background:white;
box-shadow:0 2px 10px rgba(0,0,0,.05);
">

<div style="
font-size:15px;
font-weight:600;
color:#111827;
line-height:1.45;
margin-bottom:14px;
">

{title}

</div>

<div style="
display:flex;
justify-content:space-between;
align-items:center;
flex-wrap:wrap;
gap:10px;
">

<span style="
font-size:12px;
color:#6B7280;
">

{category}

</span>

<span style="
font-size:12px;
color:#9CA3AF;
">

{time}

</span>

<span style="
background:{badge_bg};
color:{badge_text};
padding:5px 12px;
border-radius:999px;
font-size:12px;
font-weight:600;
">

{sentiment}

</span>

</div>

</div>
""",
                    unsafe_allow_html=True,
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

<h3 style="
margin-bottom:6px;
color:#16A34A;
font-size:34px;
font-weight:700;
">

BUY

</h3>

<p style="
font-size:16px;
color:#4B5563;
">

Confidence Score:
<b>92%</b>

</p>

</div>

<div class="confidence-circle">

92%

</div>

</div>

<hr>

<h4>

Why the AI recommends BUY

</h4>

<ul>

<li>
Strong quarterly earnings growth across business segments.
</li>

<li>
Positive financial news sentiment from leading media.
</li>

<li>
Healthy technical indicators (RSI & MACD).
</li>

<li>
Cloud and AI businesses continue expanding rapidly.
</li>

<li>
Institutional investors remain bullish.
</li>

</ul>

<h4>

Risk Factors

</h4>

<ul>

<li>
Market volatility due to interest rates.
</li>

<li>
Technology sector valuations remain elevated.
</li>

<li>
Global macroeconomic uncertainty.
</li>

</ul>

<p class="generated-time">

Generated just now • FinSight AI Engine

</p>

</div>
""",
            unsafe_allow_html=True,
        )

    st.write("")

    # ======================================================
    # FOOTER
    # ======================================================

    st.divider()

    footer_left, footer_center, footer_right = st.columns(
        [2, 3, 1]
    )

    with footer_left:

        st.caption("© 2026 FinSight AI")

    with footer_center:

        st.caption(
            "AI-Powered Financial Research Platform"
        )

    with footer_right:

        st.caption("v1.0")



