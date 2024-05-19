from pages import LoginPage
from secrets_environment import Secrets


class TestLoginPage:
    """Test login page."""

    def test_successful_login(self, driver):
        """Test successful login to admin page."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.fill_form_fields()
        login_page.press_enter_button()
        assert login_page.current_url == Secrets.ADMIN_DASHBOARD_PAGE_URL
