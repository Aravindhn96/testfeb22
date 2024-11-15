import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller

class Test_login():
    def __init__(self):
        self.driver = webdriver.Firefox()
    def open_login_page(self):
        self.driver.get("https://www.goibibo.com/flights")
    def login(self):
        self.driver.maximize_window()
        partial_text = "Del"
        text_to_select = "New Delhi, India"
        time.sleep(10)
        text_element = self.driver.find_element(By.XPATH, '(//p[text()="Enter city or airport"])[1]')
        text_element.click()
        keyboard = Controller()
        keyboard.type(partial_text)

        uiElement = self.driver.find_element(By.XPATH, "//*[contains(@class, 'sc-12foipm-27 fOrNYO')]")
        inner_html = uiElement.get_attribute("innerHTML")
        # print(inner_html)

        spanElement = uiElement.find_elements(By.TAG_NAME, "span")
        print(spanElement)
        
        for element in spanElement:
            if text_to_select in element.text:
                print(element.text)
                element.click()
                break 
        

        # text_element.send_keys(partial_text)

        time.sleep(10)


    def close_browser(self):
        self.driver.quit()

object_test_login = Test_login()
object_test_login.open_login_page()
object_test_login.login()
object_test_login.close_browser()














