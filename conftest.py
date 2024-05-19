import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope="session")
def driver() -> WebDriver:
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
