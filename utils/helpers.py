import streamlit as st

from data.companies import companies
from data.news import news
from data.reports import reports


def get_selected_company():
    """Return selected company from session state."""
    company = st.session_state.get("company")

    if isinstance(company, str) and company.strip():
        return company.strip()

    return "All Companies"


def get_company_options():
    """Return company options including All Companies."""
    return ["All Companies"] + sorted(companies.keys())


def render_company_selector(label="Search Company"):
    """Render company selector."""

    options = get_company_options()

    current = st.session_state.get("company", "All Companies")

    if current not in options:
        current = "All Companies"

    company = st.selectbox(
        label,
        options=options,
        index=options.index(current),
    )

    set_selected_company(company)

    return company


def set_selected_company(company):
    """Update selected company."""

    if isinstance(company, str):
        st.session_state["company"] = company.strip()


def get_company_data(company):
    """Return company information."""

    if company == "All Companies":
        company = "Apple"

    return companies.get(company, companies["Apple"])


def get_company_news(company):
    """Return company news."""

    if company == "All Companies":
        company = "Apple"

    return news.get(company, news["Apple"])


def get_company_report(company):
    """Return company report."""

    if company == "All Companies":
        company = "Apple"

    return reports.get(company, reports["Apple"])