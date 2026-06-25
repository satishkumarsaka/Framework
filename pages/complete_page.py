from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CompletePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.message_locator = (By.CLASS_NAME, "complete-header")

    def get_message_text(self):
        self.wait.until(EC.url_contains("checkout-complete"))
        return self.driver.find_element(*self.message_locator).text