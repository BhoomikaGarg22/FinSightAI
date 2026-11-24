import streamlit as st
from utils.navigation import navigate
from PyPDF2 import PdfReader
from backend.gemini.gemini_client import ask_gemini

def extract_pdf_text(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text

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

                if st.button("Analyze Report", key="analyze_report", use_container_width=True):

                 with st.spinner("Extracting PDF and generating AI insights..."):

                  extracted_text = extract_pdf_text(uploaded_file)

                  if not extracted_text.strip():
                   st.error("No readable text found in this PDF.")
                   st.stop()

                  analysis_prompt = """
                  Analyze the uploaded financial report and provide:

                  1. Executive Summary
                  2. Financial Highlights (only figures available in the report)
                  3. Key Risks
                  4. Growth Opportunities
                  5. Overall Financial Outlook

                  Do not invent any figures or information.
                  Clearly mention when information is unavailable.
                  """

                  analysis = ask_gemini(
                   question=analysis_prompt,
                   context=extracted_text[:25000]
                  )

                  st.session_state.report_analysis = analysis
                  st.session_state.report_analyzed = True
                  st.session_state.report_uploaded = True
                  st.session_state.summary = analysis

                

                if st.session_state.report_analyzed and uploaded_file is not None:
                    st.info("Analysis results are now available for the uploaded PDF.")
                

                if st.button("Test PDF Extraction"):
                 extracted_text = extract_pdf_text(uploaded_file)
                 st.write(extracted_text[:3000])

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

          
          if st.session_state.report_analyzed:

           with st.container(border=True):
            st.subheader("AI Report Analysis")
            st.success("Analysis Ready")
            st.markdown(st.session_state.report_analysis)
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