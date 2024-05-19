from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    """Represents the base page object.

    Attributes:
        driver (WebDriver): The WebDriver instance.
        url (str): The URL of the page.

    """

    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url

    @property
    def current_url(self) -> str:
        """Get current URL of the page."""
        return self.driver.current_url

    def open(self) -> None:
        """Open the page URL in browser."""
        self.driver.get(self.url)

    def find(self, *args) -> WebElement:
        """Find a web element on the page using given locator."""
        return self.driver.find_element(*args)
