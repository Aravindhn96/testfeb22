import logging
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def enter_username(self, username):
        self.logger.debug("Entering username: %s", username)
        self.driver.find_element(By.ID, "username").send_keys(username)

    def enter_password(self, password):
        self.logger.debug("Entering password")
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login_button(self):
        self.logger.debug("Clicking login button")
        self.driver.find_element(By.ID, "submit").click()


    def is_login_successful(self):
        title = self.driver.title
        self.logger.debug("Page title after login: %s", title)
        return self.driver.title == "ogged In Successfully | Practice Test Automation"
