from data.companies import companies
import streamlit as st
import pandas as pd
import plotly.express as px
import time


def show_stock_analysis():

    # ==========================================
    # PAGE HEADER
    # ==========================================

    st.title("📈 Stock Analysis")
    st.caption("Analyze any company's stock performance and AI recommendation.")

    col1, col2 = st.columns([5, 1])

    with col1:

        company = st.text_input(
            "Search Company",
            value=st.session_state.get("company", "Apple")
        )

        if company:
            st.session_state["company"] = company

    company = st.session_state.get("company", "Apple").title()

    company_data = companies.get(
        company,
        companies["Apple"]
    )

    with col2:

        st.divider()
        st.divider()

        if st.button("Analyze"):

            with st.spinner("Analyzing stock..."):
                time.sleep(2)

            st.success("✅ Analysis Complete!")

    st.divider()

    # ==========================================
    # COMPANY INFO
    # ==========================================

    st.subheader("🏢 Company Overview")

    left, right = st.columns([3, 2])

    with left:

        st.markdown("### Apple Inc.")

        st.write("**Ticker:** AAPL")

        st.write("**Sector:** Technology")

        st.write("**Industry:** Consumer Electronics")

        st.write(
            """
Apple designs, manufactures and sells smartphones,
personal computers, tablets, wearables and services.
"""
        )

    with right:

        st.metric(
            "Market Cap",
            "$2.9T"
        )

        st.metric(
            "P/E Ratio",
            "31.2"
        )

        st.metric(
            "52 Week High",
            "$199.80"
        )

    st.divider()

    # ==========================================
    # PRICE METRICS
    # ==========================================

    st.subheader("💹 Current Market Snapshot")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Current Price",
        "$189.42",
        "+2.14%"
    )

    c2.metric(
        "Open",
        "$187.50"
    )

    c3.metric(
        "Volume",
        "62.4M"
    )

    c4.metric(
        "Market Trend",
        "Bullish"
    )

    st.divider()

    # ==========================================
    # STOCK CHART
    # ==========================================

    st.subheader("📊 30-Day Price Trend")

    df = pd.DataFrame({
        "Date": pd.date_range("2025-01-01", periods=30),
        "Price": [
            180,181,182,181,183,
            184,185,186,187,188,
            187,186,188,189,190,
            191,190,192,193,194,
            193,194,195,196,197,
            196,198,199,200,201
        ]
    })

    fig = px.line(
        df,
        x="Date",
        y="Price",
        markers=True
    )

    fig.update_layout(
        height=450,
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # TECHNICAL INDICATORS
    # ==========================================

    st.subheader("📉 Technical Indicators")

    t1, t2, t3 = st.columns(3)

    with t1:
        st.metric(
            "RSI",
            "64",
            "Healthy"
        )

    with t2:
        st.metric(
            "Moving Average",
            "Bullish"
        )

    with t3:
        st.metric(
            "MACD",
            "Buy Signal"
        )

    st.divider()
    from data.companies import companies
    # ==========================================
# AI RECOMMENDATION
# ==========================================

    st.subheader("🤖 AI Recommendation")

    st.success(f"""
 ## 🟢 {company_data["recommendation"]}

 **Confidence Score:** {company_data["confidence"]}

 The stock demonstrates strong upward momentum and positive
 fundamental indicators.

 ### Reasons

 • Strong quarterly earnings

 • Positive market sentiment

 • AI-driven product growth

 • Healthy technical indicators

 • Institutional buying activity remains strong
 """)

st.divider()

    # ==========================================
    # RISK FACTORS
    # ==========================================
st.subheader("⚠ Risk Factors")

st.warning("""
• High valuation compared to industry peers

• Market volatility may affect short-term performance

• Regulatory challenges in global markets

• Rising competition in AI sector
""")

st.divider()

    # ==========================================
    # QUICK ACTIONS
    # ==========================================

st.subheader("⚡ Quick Actions")

b1, b2, b3 = st.columns(3)

with b1:
        st.button(
            "📄 Download Report",
            key="stock_download"
        )

with b2:
        st.button(
            "⭐ Add to Watchlist",
            key="stock_watchlist"
        )

with b3:
        st.button(
            "🤖 Ask AI",
            key="stock_ai"
        )

st.divider()

st.caption(
        "© 2026 FinSight AI | AI-Powered Financial Research Platform"
    )