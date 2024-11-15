import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Iframe():
    def switchto_iframe(self):
        driver = webdriver.Firefox()
        driver.get("https://www.letskodeit.com/practice")
        driver.maximize_window()
        driver.execute_script("window.scrollBy(0,1000);")
        driver.switch_to.frame("courses-iframe1")
        driver.execute_script("window.scrollBy(0,1000);")
        driver.switch_to.parent_frame()
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,-1000);")
ss = Iframe()
ss.switchto_iframe()



# No Such Element Exception
# Timeout Exception
# Stale Element Reference Exception
# Element Not interactable Exception
# Element click intercepted Exception
# No such window Exception
# No frame exception
# unhandled Alert exception

Pytest