from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from secrets_environment import Secrets


class AdminDashboardPage(BasePage):
    """Represent admin dashboard page."""

    LAST_TABLE_ELEMENT_SELECTOR = (
        By.CSS_SELECTOR,
        "table tbody tr:last-child",
    )

    def __init__(
        self,
        driver: WebDriver,
        url: str = Secrets.ADMIN_DASHBOARD_PAGE_URL,
    ):
        super().__init__(driver, url)

    @property
    def get_last_post_data(self) -> list[str]:
        """Retrieve the data from the last row in the table with posts."""
        last_table_row = self.find(*self.LAST_TABLE_ELEMENT_SELECTOR)
        last_table_row_data = last_table_row.find_elements(By.TAG_NAME, "td")
        last_post_data_list = []
        for td in last_table_row_data:
            last_post_data_list.append(td.text)
        return last_post_data_list
