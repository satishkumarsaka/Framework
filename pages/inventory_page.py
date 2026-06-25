from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.backpack_locator = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_locator = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack(self):
        self.wait.until(EC.url_contains("inventory"))
        self.driver.find_element(*self.backpack_locator).click()

    def click_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_locator)).click()