from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username_locator = (By.ID, "user-name")
        self.password_locator = (By.ID, "password")
        self.login_locator = (By.ID, "login-button")
        self.error_locator = (By.CSS_SELECTOR, "[data-test='error']")

    def enter_username(self, text):
        self.driver.find_element(*self.username_locator).send_keys(text)

    def enter_password(self, text):
        self.driver.find_element(*self.password_locator).send_keys(text)

    def click_login(self):
        self.driver.find_element(*self.login_locator).click()

    def get_error_text(self):
        return self.driver.find_element(*self.error_locator).text