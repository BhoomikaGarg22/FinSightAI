import streamlit as st

from data.companies import companies
from data.news import news
from data.reports import reports


def get_selected_company():
    """Return selected company from session state."""
    return (
        st.session_state
        .get("company", "Apple")
        .strip()
        .title()
    )


def set_selected_company(company):
    """Update selected company."""
    st.session_state["company"] = company.strip().title()


def get_company_data(company):
    """Return company information."""
    return companies.get(company, companies["Apple"])


def get_company_news(company):
    """Return news list."""
    return news.get(company, news["Apple"])


def get_company_report(company):
    """Return report summary."""
    return reports.get(company, reports["Apple"])