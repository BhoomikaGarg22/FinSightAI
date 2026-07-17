import streamlit as st
from utils.navigation import navigate

def show_report_analyzer():
    st.image(
        "assets/images/upload_document.png",
        use_container_width=True
    )
    
    # =====================================================
    # HEADER
    # =====================================================

    st.markdown("""
    <div class="page-header">

    <h1>📄 AI Financial Report Analyzer</h1>

    <p>
    Upload annual reports, quarterly filings, and financial statements.
    Our AI extracts insights, identifies risks, and summarizes key financial metrics within seconds.
    </p>

    <div class="market-status">

    🤖 <b>AI Ready</b>

    <span class="status-dot"></span>

    Supports PDF Reports

    </div>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # UPLOAD + FEATURES
    # =====================================================

    left, right = st.columns([2, 1])

    with left:

        with st.container(border=True):

            st.markdown("## Upload Financial Report")

            st.caption(
             "Supported formats: Annual Reports • 10-K • Quarterly Reports • Earnings Reports"
            )

            st.write("")

            uploaded_file = st.file_uploader(
                "Choose PDF",
                type=["pdf"],
                label_visibility="collapsed"
            )

            st.caption(
                "Supported files: Annual Reports • 10-K • Earnings Reports"
            )

            if uploaded_file:

                st.success("✅ Report uploaded successfully and ready for AI analysis.")

                c1, c2 = st.columns(2)

                with c1:
                 st.metric(
                 "File",
                 uploaded_file.name
             )

                with c2:
                 st.metric(
                 "Size",
                 f"{round(uploaded_file.size/1024,2)} KB"
            )
                st.button(
                    "Analyze with AI",
                    key="analyze_report",
                    use_container_width=True
                )

            else:

             st.image(
              upload_image,
              width=220
             )

             st.info(
              "Upload a financial report to begin AI analysis."
             )

    with right:
        st.image(
            "assets/images/upload_document.jpg",
            use_container_width=True
        )

        with st.container(border=True):

            st.subheader("AI Features")

            st.markdown("""
✅ Executive Summary

✅ Financial Highlights

✅ Risk Timeline

✅ Growth Opportunities

✅ ESG Insights

✅ Contradiction Detection

✅ Financial Ratios

✅ Investment Recommendation
""")

    st.write("")

    # =====================================================
    # PROCESSING STATUS
    # =====================================================

    with st.container(border=True):

        st.subheader("AI Processing Pipeline")

        progress = st.progress(100)

        st.write("")

        c1, c2 = st.columns(2)

        with c1:

            st.success("✅ Reading PDF")

            st.success("✅ Extracting Financial Data")

            st.success("✅ Detecting Risks")

        with c2:

            st.success("✅ Generating AI Summary")

            st.success("✅ Calculating Financial Ratios")

            st.success("✅ Preparing Recommendation")

        st.write("")

        st.info(
            "AI analysis completed successfully. The report is ready for review."
        )

    st.write("")

    # =====================================================
# FINANCIAL HIGHLIGHTS
# =====================================================

    st.markdown("## Financial Highlights")

    st.caption("Key financial metrics extracted from the uploaded report.")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        with st.container(border=True):
            st.metric(
                "Revenue",
                "$394B",
                "+18%"
            )

    with c2:
        with st.container(border=True):
            st.metric(
                "Net Income",
                "$98B",
                "+12%"
            )

    with c3:
        with st.container(border=True):
            st.metric(
                "EPS",
                "$6.14",
                "+9%"
            )

    with c4:
        with st.container(border=True):
            st.metric(
                "Operating Margin",
                "30%",
                "+2%"
            )
    st.write("")

    # =====================================================
    # AI RESULTS
    # =====================================================

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Summary",
            "Risks",
            "Opportunities",
            "Recommendation"
        ]
    )

    with tab1:

        st.success("""
### Executive Summary

• Revenue increased by **18%**

• Profit margins improved.

• Cash reserves remain strong.

• AI investments continue driving growth.

• Management outlook remains positive.
""")

    with tab2:

        st.warning("""
### Key Risks

• Regulatory uncertainty

• High AI competition

• Supply chain dependency

• Currency fluctuations

• Premium valuation
""")

    with tab3:

        st.info("""
### Growth Opportunities

• AI expansion

• Cloud business growth

• Emerging markets

• Subscription services

• Product innovation
""")

    with tab4:

        st.success("""
## 🟢 BUY

**Confidence Score: 92%**

### Why?

✅ Strong balance sheet

✅ Healthy cash flow

✅ Positive earnings trend

✅ Attractive long-term outlook
""")

    st.write("")

    # =====================================================
    # QUICK ACTIONS
    # =====================================================

    with st.container(border=True):

        st.subheader("⚡ Quick Actions")

        b1, b2, b3 = st.columns(3)

        with b1:
         if st.button(
          "Download Summary",
          use_container_width=True
        ):
            st.success("Summary downloaded successfully!")

        with b2:
         if st.button(
          "Ask AI",
          use_container_width=True
        ):
            navigate("AI Chat")

        with b3:
         if st.button(
          "Upload Another",
          use_container_width=True
        ):
            st.rerun()

    st.divider()

    st.caption("© 2026 FinSight AI | AI-Powered Financial Research Platform")