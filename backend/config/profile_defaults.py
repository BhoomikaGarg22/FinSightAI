import copy

DEFAULT_PROFILE = {

    # --------------------------------------------------
    # Personal Information
    # --------------------------------------------------
    "display_name": "",
    "phone": "",
    "country": "India",
    "occupation": "Student",

    # --------------------------------------------------
    # Investor Profile
    # --------------------------------------------------
    "investor_type": "Investor",
    "risk_appetite": "Moderate",
    "investment_experience": "Beginner",
    "investment_horizon": "Long Term",

    # --------------------------------------------------
    # Investment Goals
    # --------------------------------------------------
    "investment_goals": [],

    # --------------------------------------------------
    # Preferred Markets
    # --------------------------------------------------
    "markets": [],

    # --------------------------------------------------
    # AI Preferences
    # --------------------------------------------------
    "ai_style": "Balanced",
    "response_length": "Medium",
    "preferred_region": "Global",
    "default_dashboard": "Overview",

    # --------------------------------------------------
    # Appearance
    # --------------------------------------------------
    "theme": "System",
    "accent_color": "Blue",
    "compact_dashboard": False,
    "animations": True,

    # --------------------------------------------------
    # Localization
    # --------------------------------------------------
    "language": "English",
    "currency": "USD",

    # --------------------------------------------------
    # Notifications
    # --------------------------------------------------
    "notifications": {
        "daily_summary": True,
        "market_news": True,
        "ai_alerts": False,
        "price_alerts": False,
        "earnings": True,
        "weekly_ai": False,
    },
}


JSON_FIELDS = {
    "investment_goals",
    "markets",
    "notifications",
}


def get_default_profile():
    """
    Returns a deep copy of the default profile.

    Using deepcopy ensures mutable fields like lists and
    dictionaries are independent for each user.
    """
    return copy.deepcopy(DEFAULT_PROFILE)