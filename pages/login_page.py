from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from secrets_environment import Secrets


class LoginPage(BasePage):
    """Represent login page."""

    ENTER_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[type='submit']")
    EMAIL_FIELD_LOCATOR = (By.ID, "email")
    PASSWORD_FIELD_LOCATOR = (By.ID, "password")

    def __init__(
        self,
        driver: WebDriver,
        url: str = Secrets.LOGIN_PAGE_URL,
    ):
        super().__init__(driver, url)

    def fill_form_fields(self) -> None:
        """Fill email and password fields."""
        email_field = self.find(*self.EMAIL_FIELD_LOCATOR)
        email_field.send_keys(Secrets.LOGIN)
        password_field = self.find(*self.PASSWORD_FIELD_LOCATOR)
        password_field.send_keys(Secrets.PASSWORD)

    def press_enter_button(self) -> None:
        """Press enter button to submit the form."""
        enter_button = self.find(*self.ENTER_BUTTON_LOCATOR)
        enter_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(Secrets.ADMIN_DASHBOARD_PAGE_URL),
        )
