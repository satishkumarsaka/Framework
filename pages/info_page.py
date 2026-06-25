from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InfoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.first_name_locator = (By.ID, "first-name")
        self.last_name_locator = (By.ID, "last-name")
        self.zip_code_locator = (By.ID, "postal-code")
        self.continue_locator = (By.ID, "continue")

    def enter_first_name(self, text):
        self.wait.until(EC.url_contains("checkout-step-one"))
        self.wait.until(EC.element_to_be_clickable(self.first_name_locator)).send_keys(text)

    def enter_last_name(self, text):
        self.driver.find_element(*self.last_name_locator).send_keys(text)

    def enter_zip_code(self, text):
        self.driver.find_element(*self.zip_code_locator).send_keys(text)

    def click_continue(self):
        self.driver.find_element(*self.continue_locator).click()