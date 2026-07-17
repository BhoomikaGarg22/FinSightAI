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

from components.ui_components import (
    section_title,
    metric_card,
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

    st.title("Stock Analysis")

    st.caption(
        "AI-powered stock analysis and investment insights."
    )

    st.divider()

    # ===========================
    # Search
    # ===========================

    col1, col2 = st.columns([5, 1])

    with col1:

        search = st.text_input(
            "Search Company",
            value=company,
            placeholder="Apple, Tesla, NVIDIA..."
        )

    with col2:

        st.write("")
        st.write("")

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

    section_title("Company Overview")

    left, right = st.columns([3, 2])

    with left:

      with st.container(border=True):

        st.markdown(f"### {company}")

        st.write(f"**Ticker:** {company_data['ticker']}")

        st.write(f"**Sector:** {company_data['sector']}")

        st.write(f"**Industry:** {company_data['industry']}")

        st.write("")

        st.write(company_data["description"])

    with right:

      with st.container(border=True):

        st.markdown("### Company Statistics")

        st.metric(
            "Market Cap",
            company_data["market_cap"]
        )

        st.metric(
            "P/E Ratio",
            company_data["pe_ratio"]
        )

        st.metric(
            "52 Week High",
            company_data["high_52"]
        )

        st.metric(
            "Trend",
            company_data["trend"]
        )

    # ===========================
# Market Snapshot
# ===========================

    st.divider()

    section_title("Market Snapshot")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
     metric_card(
        "Current Price",
        company_data["price"],
        "+2.14%"
    )

    with c2:
     metric_card(
        "Market Cap",
        company_data["market_cap"]
    )

    with c3:
     metric_card(
        "P/E Ratio",
        company_data["pe_ratio"]
    )

    with c4:
     metric_card(
        "52 Week High",
        company_data["high_52"]
    )
     
     st.divider()

    section_title("30-Day Stock Performance")

    chart_df = get_chart_data(company)

    fig = px.line(
     chart_df,
     x="Date",
     y="Price",
     markers=True
)

    fig.update_layout(
     template="plotly_dark",
     height=450,
     paper_bgcolor="rgba(0,0,0,0)",
     plot_bgcolor="rgba(0,0,0,0)",
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

    section_title("Technical Indicators")

    c1, c2, c3 = st.columns(3)

    with c1:
     metric_card(
        "RSI",
        company_data["rsi"]
    )

    with c2:
     metric_card(
        "Moving Average",
        company_data["moving_average"]
    )

    with c3:
     metric_card(
        "MACD",
        company_data["macd"]
    )
     
     st.divider()

    section_title("AI Recommendation")

    recommendation_card(
     company_data["recommendation"],
     company_data["confidence"]
)
