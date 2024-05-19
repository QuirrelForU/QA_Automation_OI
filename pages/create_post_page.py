import platform
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from secrets_environment import Secrets


class CreatePostPage(BasePage):
    """Represent create post page."""

    CREATE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[type='submit']")
    POST_TITLE_LOCATOR = (By.ID, "title")
    POST_CONTENT_LOCATOR = (By.CSS_SELECTOR, ".ql-editor")
    POST_AUTHOR_LOCATOR = (By.ID, "author")
    SUCCESSFUL_NOTIFICATION_LOCATOR = (By.CSS_SELECTOR, ".alert-success")

    TEST_DATA = {
        "Title": "HK Quote",
        "Content": "Isn't this a wonderful spot for a rest? "
        "I so love the sound of the rain upon glass",
        "Author": "Quirrel",
    }

    def __init__(
        self,
        driver: WebDriver,
        url: str = Secrets.CREATE_PAGE_URL,
    ):
        super().__init__(driver, url)

    def fill_post_fields(self) -> None:
        """Fill fields for creating a post."""
        post_title = self.find(*self.POST_TITLE_LOCATOR)
        post_title.send_keys(self.TEST_DATA["Title"])
        post_content = self.find(*self.POST_CONTENT_LOCATOR)
        post_content.send_keys(self.TEST_DATA["Content"])
        post_author = self.find(*self.POST_AUTHOR_LOCATOR)
        post_author.send_keys(self.TEST_DATA["Author"])

    def click_create_button(self) -> None:
        """Click on create button."""
        create_button = self.find(*self.CREATE_BUTTON_LOCATOR)
        create_button.click()

    @property
    def get_notification_message(self) -> str:
        """Get the text of the successful notification."""
        successful_notification = self.find(
            *self.SUCCESSFUL_NOTIFICATION_LOCATOR,
        )
        return successful_notification.text

    @property
    def get_post_creation_time(self) -> str:
        """Get the current date and time."""
        now = datetime.now()
        if platform.system() == "Windows":
            formatted_time = now.strftime("%B %#d, %Y, %#I:%M:%S %p")
        else:
            formatted_time = now.strftime("%B %-d, %Y, %-I:%M:%S %p")

        return formatted_time
