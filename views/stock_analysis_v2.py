import streamlit as st
import time
import plotly.express as px

from components.ui_components import (
    section_title,
    metric_card,
    recommendation_card,
)

from utils.helpers import (
    get_selected_company,
    set_selected_company,
    get_company_data,
)

from data.charts import get_chart_data

def show_stock_analysis_v2():

    # ===========================
    # Load selected company
    # ===========================

    company = get_selected_company()
    company_data = get_company_data(company)

    # ===========================
    # Header
    # ===========================

    st.markdown(
        """
    <div class="page-header">

    <h1>📈 Stock Analysis</h1>

    <p>
    Analyze publicly traded companies using AI-powered financial insights,
    technical indicators, and market trends.
    </p>

    <div class="market-status">

    🟢 <b>Market Open</b>

    <span class="status-dot"></span>

    Last Updated: 2 mins ago

    </div>

    </div>
    """,
        unsafe_allow_html=True,
    )

    # ===========================
    # Search
    # ===========================

    col1, col2 = st.columns([6, 1])

    with col1:

        search = st.text_input(
            "Search Company",
            value=company,
            placeholder="Apple, Tesla, NVIDIA..."
        )

    with col2:

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button(
            "Analyze",
            key="stock_v2_analyze",
            use_container_width=True
        ):

            set_selected_company(search)

            with st.spinner("Analyzing company..."):
                time.sleep(2)

            st.rerun()

    company = get_selected_company()
    company_data = get_company_data(company)

    st.divider()

    # ===========================
# Company Overview
# ===========================

    st.divider()

    section_title("🏢 Company Overview")
    st.caption("Company profile and key business information.")
    left, right = st.columns([3, 2])

    with left:

      with st.container(border=True):

        st.markdown(f"## 🍎 {company}")

        st.markdown(
            f"""
     **🏷️ Ticker:** `{company_data['ticker']}`

     **🏢 Sector:** {company_data['sector']}

     **💻 Industry:** {company_data['industry']}
     """
        )

        st.divider()

        st.markdown("### 📖 About Company")

        st.write(company_data["description"])

    with right:

      with st.container(border=True):

        st.markdown("## 📊 Company Statistics")

        st.metric(
         label="💰 Market Cap",
         value=company_data["market_cap"]
        )

        st.metric(
         label="📈 P/E Ratio",
         value=company_data["pe_ratio"]
        )

        st.metric(
         label="🚀 52 Week High",
         value=company_data["high_52"]
        )

        trend = company_data["trend"]

        if trend.lower() == "bullish":
         st.success("🟢 Bullish")

        elif trend.lower() == "bearish":
         st.error("🔴 Bearish")

        else:
         st.warning("🟡 Neutral")

    # ===========================
# Market Snapshot
# ===========================

    st.divider()

    section_title("📊 Market Snapshot")
    st.caption("Real-time stock metrics and valuation indicators.")
    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
     metric_card(
        "💵 Current Price",
        company_data["price"],
        "+2.14%"
     )

    with c2:
     metric_card(
        "💰 Market Cap",
        company_data["market_cap"]
    )

    with c3:
     metric_card(
        "📈 P/E Ratio",
        company_data["pe_ratio"]
    )

    with c4:
     metric_card(
        "🚀 52 Week High",
        company_data["high_52"]
    )
     
    with c5:
        metric_card(
            "📈 Avg Volume",
            "78.2M"
        )
     
        st.divider()

    section_title("📈 30-Day Stock Performance")
    st.caption("Historical stock performance over the last 30 trading days.")

    t1, t2, t3, t4, t5 = st.columns(5)

    with t1:
        st.button("1D", disabled=True, use_container_width=True)

    with t2:
        st.button("1W", disabled=True, use_container_width=True)

    with t3:
        st.button("1M", use_container_width=True)

    with t4:
        st.button("6M", disabled=True, use_container_width=True)

    with t5:
        st.button("1Y", disabled=True, use_container_width=True)
    
    
    chart_df = get_chart_data(company)

    fig = px.line(
        chart_df,
        x="Date",
        y="Price",
        markers=True,
    )

    fig.update_traces(

        line=dict(
            color="#4F46E5",
            width=3,
            shape="spline"
        ),

        marker=dict(
            size=7
        ),

        fill="tozeroy",

        fillcolor="rgba(79,70,229,0.10)"
    )

    fig.update_layout(

        template="plotly_white",

        height=500,

        paper_bgcolor="white",

        plot_bgcolor="white",

        margin=dict(l=15, r=15, t=25, b=20),

        hovermode="x unified",

        xaxis_title="",

        yaxis_title="Price ($)",

        legend_title="",

        font=dict(
            size=14,
            color="#374151"
        ),

    )

    fig.update_xaxes(
        showgrid=False
    )

    fig.update_yaxes(
        gridcolor="#E5E7EB"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displayModeBar": False
        }
    )
    
    st.divider()

    section_title("📉 Technical Indicators")
    st.caption("Key technical signals based on historical price trends.")

    c1, c2, c3 = st.columns(3)

    # ---------------- RSI ---------------- #

    with c1:

        with st.container(border=True):

            st.markdown("### 📉 RSI")

            st.markdown(f"## {company_data['rsi']}")

            st.warning("🟠 Overbought")

            st.caption(
                "The stock may be approaching a short-term pullback."
            )

    # ---------------- MACD ---------------- #

    with c2:

        with st.container(border=True):

            st.markdown("### 📈 MACD")

            st.markdown(f"## {company_data['macd']}")

            st.success("🟢 Bullish Signal")

            st.caption(
                "Momentum indicates continued buying interest."
            )

     # ---------------- Moving Average ---------------- #

    with c3:

        with st.container(border=True):

            st.markdown("### 📊 Moving Average")

            st.markdown(f"## {company_data['moving_average']}")

            st.success("✅ Above 50 DMA")

            st.caption(
                "The stock remains in an overall upward trend."
            )
     
        st.divider()

    section_title("🤖 AI Investment Recommendation")

    st.caption(
        "AI-generated investment outlook based on market trends and technical indicators."
    )

    with st.container(border=True):

        left, right = st.columns([4,1])

    # ---------------- LEFT ---------------- #

        with left:
            recommendation = company_data["recommendation"].upper()

            if recommendation == "BUY":
             st.success(f"### 🟢 {recommendation}")

            elif recommendation == "SELL":
             st.error(f"### 🔴 {recommendation}")

            else:
             st.warning(f"### 🟡 {recommendation}")
            

            st.markdown("### ✅ Why AI recommends this")

            st.markdown("""
    - Strong quarterly earnings

    - Positive market sentiment

    - Healthy technical indicators

    - Consistent revenue growth
    """)

            st.markdown("### ⚠ Risks to Consider")

            st.markdown("""
    - Market volatility

    - Global macroeconomic uncertainty

    - Premium valuation
    """)

            st.markdown("### 📄 Overall Outlook")

            st.write(
                f"""
    {company} continues to demonstrate strong financial health with
    steady growth and positive investor sentiment.

    Based on current market conditions and technical indicators,
    our AI model suggests a **{company_data['recommendation']}**
    rating for medium to long-term investors.
    """
            )

    # ---------------- RIGHT ---------------- #

        with right:

            st.markdown("### Confidence")

            st.markdown(
                f"""
    <div class="confidence-circle">
    {company_data['confidence']}
    </div>
    """,
                unsafe_allow_html=True,
            )

            st.info(
    "💡 **Disclaimer:** This recommendation is generated for educational purposes and should not be considered financial advice."
)
            
            st.divider()

    section_title("📊 Key Financial Ratios")

    st.caption(
        "Important financial metrics for evaluating company performance."
    )

    r1, r2, r3 = st.columns(3)

    with r1:

        with st.container(border=True):

            st.metric(
                "Revenue Growth",
                "+12.4%"
            )

            st.metric(
                "Net Margin",
                "18.2%"
            )

    with r2:

        with st.container(border=True):

            st.metric(
                "EPS",
                "$6.18"
            )

            st.metric(
                "ROE",
                "24.3%"
            )

    with r3:

        with st.container(border=True):

            st.metric(
                "Dividend Yield",
                "0.48%"
            )

            st.metric(
                "Debt / Equity",
                "1.12"
            )

            st.write("")

    section_title("📝 AI Executive Summary")

    st.caption(
        "Quick AI-generated overview of the company's current outlook."
    )

    with st.container(border=True):

        st.markdown(
            f"""
    ### {company} Outlook

    Our AI analysis indicates that **{company}**
    continues to demonstrate strong financial stability,
    healthy revenue growth, and positive technical momentum.

    **Key Highlights**

    ✅ Strong earnings performance
 
    ✅ Positive institutional sentiment

    ✅ Healthy technical indicators

    ⚠ Keep an eye on market volatility
    and valuation levels.

    **Overall Rating:** **{company_data['recommendation']}**
    """
        )
