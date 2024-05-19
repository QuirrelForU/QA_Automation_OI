import os


class Secrets:
    """GitHub's secrets variables for GitHub actions."""

    LOGIN = os.environ.get("TEST_LOGIN")
    PASSWORD = os.environ.get("TEST_PASSWORD")
    LOGIN_PAGE_URL = os.environ.get("TEST_LOGIN_PAGE_URL")
    ADMIN_DASHBOARD_PAGE_URL = os.environ.get(
        "TEST_ADMIN_DASHBOARD_PAGE_URL",
    )
    CREATE_PAGE_URL = os.environ.get("TEST_CREATE_PAGE_URL")
