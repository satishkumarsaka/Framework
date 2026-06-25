from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OverviewPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.finish_locator = (By.ID, "finish")

    def click_finish(self):
        self.wait.until(EC.url_contains("checkout-step-two"))
        self.wait.until(EC.element_to_be_clickable(self.finish_locator)).click()