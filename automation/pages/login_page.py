# automation/pages/login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # --- Locators ---
    USERNAME_FIELD = (By.CSS_SELECTOR, '[data-test="username"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[data-test="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-test="login-button"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        element = self.wait.until(
            EC.presence_of_element_located(self.USERNAME_FIELD))
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        element = self.wait.until(
            EC.presence_of_element_located(self.PASSWORD_FIELD))
        element.clear()
        element.send_keys(password)

    def click_login(self):
        element = self.wait.until(
            EC.presence_of_element_located(self.LOGIN_BUTTON))
        element.click()

    def get_error_message(self):
        element = self.wait.until(
            EC.presence_of_element_located(self.ERROR_MESSAGE))
        return element.text

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
