import streamlit as st
import pandas as pd
import plotly.express as px
from data.companies import companies
from utils.navigation import navigate
def show_watchlist():

    st.markdown("""
    <div class="page-header">

    <h1>Watchlist</h1>

    <p>
    Track your favorite companies, monitor price movements,
    and receive AI-powered market insights.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.subheader("Add Stock")

    left, right = st.columns([6, 1])

    company_list = sorted(companies.keys())

    with left:

        selected_company = st.selectbox(
            "",
            company_list,
            index=None,
            placeholder="Search company...",
            label_visibility="collapsed"
        )

    with right:

     if st.button(
        "Add",
        use_container_width=True
    ):

        if "watchlist" not in st.session_state:
            st.session_state.watchlist = []

        if selected_company:

            if selected_company not in st.session_state.watchlist:

                st.session_state.watchlist.append(selected_company)

                st.success(f"{selected_company} added to Watchlist.")

                st.rerun()

            else:

                st.warning("Already in Watchlist.")

    st.write("")

    st.subheader("Watchlist Summary")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Stocks", "12")
    c2.metric("Gainers", "8")
    c3.metric("Losers", "4")
    c4.metric("Avg Change", "+2.3%")

    st.write("")

    left, right = st.columns([2,1])

    with left:
        if "watchlist" not in st.session_state:

         st.session_state.watchlist = [
            "Apple",
            "NVIDIA",
            "Tesla"
        ]
        st.subheader("Current Watchlist")

        for company in st.session_state.watchlist:

         company_data = companies[company]

        with st.container(border=True):

            col1, col2, col3 = st.columns([4,2,2])

            with col1:
                st.markdown(f"### {company}")
                st.caption(
                 f"{company_data['ticker']} • {company_data['sector']}"
                )

            with col2:
                st.metric(
                    "Price",
                    company_data["price"],
                    company_data["change"]
                )
                st.caption(f"AI Rating: {company_data['recommendation']}")
            with col3:

                if st.button(
                    "Analyze",
                    key=f"a_{company}",
                    use_container_width=True
                ):
                    navigate(
                        "Stock Analysis",
                        company=company
                    )

                if st.button(
                    "Remove",
                    key=f"r_{company}",
                    use_container_width=True
                ):

                    st.session_state.watchlist.remove(company)

                    st.rerun()

    with right:

     st.write("")

    st.subheader("AI Insights")

    with st.container(border=True):

        st.markdown("""

    ### Market Overview

    Apple and NVIDIA continue to show strong momentum.

    Microsoft remains stable with consistent growth.

    Tesla is currently experiencing higher volatility.

    Overall watchlist sentiment remains positive.

    """)
        
    st.write("")

    st.subheader("Quick Actions")

    b1, b2, b3 = st.columns(3)

    with b1:

        if st.button(
         "Refresh Prices",
         use_container_width=True
        ):

         st.toast("Prices refreshed")

         st.rerun()

    with b2:

        if st.button(
         "Analyze Watchlist",
         use_container_width=True
        ):

         st.info("AI analysis coming soon.")

    with b3:

        import pandas as pd

        df = pd.DataFrame(
         {"Company": st.session_state.watchlist}
        )

        csv = df.to_csv(index=False)

        st.download_button(
         "Export Watchlist",
         csv,
         "watchlist.csv",
         "text/csv",
         use_container_width=True
        )

    st.divider()

st.caption("© 2026 FinSight AI | AI-Powered Financial Research Platform")    
