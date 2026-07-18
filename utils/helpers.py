import streamlit as st

from data.companies import companies
from data.news import news
from data.reports import reports


def get_selected_company():
    """Return selected company from session state."""
    company = st.session_state.get("company")
    if isinstance(company, str) and company.strip():
        return company.strip().title()
    return None


def get_company_options():
    """Return sorted company options for dropdown selectors."""
    return sorted(companies.keys())


def render_company_selector(label="Search companies"):
    """Render a dropdown company selector with a placeholder hint only."""
    options = sorted(companies.keys())
    company = st.selectbox(
        label,
        options=options,
        index=None,
        placeholder="Search companies"
    )

    if company and company.strip():
        set_selected_company(company)
        return company

    return None


def set_selected_company(company):
    """Update selected company."""
    if isinstance(company, str) and company.strip():
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