import time
import logging
import pytest
from selenium import webdriver

# Configure logging
logging.basicConfig(filename='logs/test.log',
                    level=logging.DEBUG)

# Set up a logger for this module
logger = logging.getLogger(__name__)

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(3)
    yield driver
    driver.quit()