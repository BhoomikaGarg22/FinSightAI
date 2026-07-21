import streamlit as st
from utils.navigation import navigate


def show_report_analyzer():

    if "report_analyzed" not in st.session_state:
        st.session_state.report_analyzed = False

    # =====================================================
    # HEADER
    # =====================================================

    st.title("AI Financial Report Analyzer")
    st.caption("Upload an annual report and let AI extract financial insights in seconds.")

    # =====================================================
    # UPLOAD + FEATURES
    # =====================================================

    left, right = st.columns([2, 1])

    with left:

        with st.container(border=True):

            st.subheader("Upload Financial Report")

            uploaded_file = st.file_uploader(
                "Choose PDF",
                type=["pdf"],
                label_visibility="collapsed"
            )

            st.caption(
                "Supported files: Annual Reports • 10-K • Earnings Reports"
            )

            if uploaded_file is not None:

                st.success("File Uploaded Successfully")

                st.write(f"**File:** {uploaded_file.name}")
                st.write(f"**Size:** {round(uploaded_file.size/1024,2)} KB")

                if uploaded_file.type and uploaded_file.type.startswith("image/"):
                    st.image(uploaded_file, caption=uploaded_file.name, use_column_width=True)

                if st.button(
                    "Analyze Report",
                    key="analyze_report",
                    use_container_width=True
                ):
                    st.session_state.report_analyzed = True
                    st.session_state.report_uploaded = True
                    st.session_state.uploaded_file = uploaded_file
                    st.success("Report analysis started successfully")

                if st.session_state.report_analyzed and uploaded_file is not None:
                    st.info("Analysis results are now available for the uploaded PDF.")
                
                else:

                 st.info(
                    "Upload a financial report to begin AI analysis."
                )

    with right:

             with st.container(border=True):

               st.subheader("AI Features")

               st.markdown("""
               Executive Summary

               Financial Highlights

               Risk Timeline

               Growth Opportunities

               ESG Insights

               Contradiction Detection

               Financial Ratios

               Investment Recommendation
               """)

             st.write("")

    if st.session_state.report_analyzed and uploaded_file is not None:

        # =====================================================
        # PROCESSING STATUS
        # =====================================================

          with st.container(border=True):

            st.subheader("Processing Status")

            st.progress(100)

            st.success("Analysis Ready")

          st.write("")

        # =====================================================
        # FINANCIAL METRICS
        # =====================================================

          st.subheader("Financial Highlights")

          c1, c2, c3, c4 = st.columns(4)
          c1.metric("Revenue", "$394B", "+18%")
          c2.metric("Net Income", "$98B", "+12%")
          c3.metric("EPS", "$6.14", "+9%")
          c4.metric("Operating Margin", "30%", "+2%")

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
         ## BUY

         **Confidence Score: 92%**

         ### Why?

         Strong balance sheet

         Healthy cash flow

         Positive earnings trend

         Attractive long-term outlook
         """)

          st.write("")
          summary = """
          Executive Summary

          • Revenue increased by 18%

          • Profit margins improved.

          • Cash reserves remain strong.

          • AI investments continue driving growth.

          • Management outlook remains positive.

          Recommendation: BUY

          Confidence: 92%
          """
    # =====================================================
    # QUICK ACTIONS
    # =====================================================

    with st.container(border=True):

         st.subheader("Quick Actions")

         b1, b2, b3 = st.columns(3)

         with b1:

           st.download_button(
            label="Download Summary",
            data=st.session_state.get("summary", ""),
            file_name="Financial_Report_Summary.txt",
            mime="text/plain",
            use_container_width=True,
            disabled="summary" not in st.session_state
        )

         with b2:
            if st.button("Ask AI", use_container_width=True):
               st.session_state.report_uploaded = True
               navigate("AI Chat")
               
         with b3:
            if st.button(
             "Upload Another",
             use_container_width=True
         ):

             st.session_state.report_analyzed = False
             st.session_state.pop("uploaded_file", None)
             st.session_state.pop("report_uploaded", None)

             st.rerun()     

    st.divider()
    st.caption("© 2026 FinSight AI | AI-Powered Financial Research Platform")