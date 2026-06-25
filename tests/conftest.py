from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()

    yield driver

    driver.quit()