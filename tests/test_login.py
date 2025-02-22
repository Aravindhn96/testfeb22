import configparser
import pytest
from pages.login_page import LoginPage
import logging

# Configure logger for the test file
logger = logging.getLogger(__name__)

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')


def test_login(driver):
    login_page = LoginPage(driver)

    # Read credentials from config
    username = config.get('login', 'username')
    password = config.get('login', 'password')

    logger.info("Starting login test with username: %s", username)

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()
    logger.info("Login button clicked")

    assert login_page.is_login_successful()
    logger.info("Login successful with title: %s", driver.title)

