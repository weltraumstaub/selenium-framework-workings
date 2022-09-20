"""
This module contains Client Login Page Information,
the page object for the Client Login page.
"""


from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

class ClientLoginPage:

    # url 
    URL = "https://stage.psyedge.ru/Client/RegistrationLoginPage"
   
    # locators  
    COOKIES_BUTTON = (By.CSS_SELECTOR, "button.button.primary.size-55")  
    POLICY_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    PHONE_NUMBER_INPUT = (By.CSS_SELECTOR, "input[type='phone']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn-enter")

    # initiation
    def __init__(self, browser):
        self.browser = browser

    # load 
    def load(self):
        self.browser.get(self.URL)

    # accept cookie policy 
    def accept_cookies(self): 
        cookies_button = self.browser.find_element(*self.COOKIES_BUTTON)
        cookies_button.click()

    # accept website privacy policies 
    def accept_site_policy(self): 
        policy_checkbox = self.browser.find_element(*self.POLICY_CHECKBOX)
        policy_checkbox.click()

    # enter phone number 
    def input_phone_number(self): 
        phone_number_input = self.browser.find_element(*self.PHONE_NUMBER_INPUT)
        phone_number_input.click().send_keys("9999999999")

    # proceed to login into the system 
    def click_login_button(self): 
        login_button = self.browser.find_element(*self.LOGIN_BUTTON)
        login_button.click()


    
