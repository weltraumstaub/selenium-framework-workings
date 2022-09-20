"""
This module contains Landing Page Information,
the page object for the Landing page.
"""

from selenium.webdriver.common.by   import By
from selenium.webdriver.common.keys import Keys


class MainPage:

    # url 
    URL = "https://stage.psyedge.ru"
    
    # locators
    COOKIES_BUTTON = (By.CSS_SELECTOR, "button.button.primary.size-55")  
    ARROW_DOWN = (By.CSS_SELECTOR, "button.btn")
    CLIENT_LOGIN = (By.CSS_SELECTOR, "a[href='/Client/RegistrationLoginPage']")
    PSYCHOLOGIST_LOGIN = (By.CSS_SELECTOR, "a[href='/Client/LoginPage']")
    LOGIN_MENU_BUTTON = (By.CSS_SELECTOR, "button.menu-button")

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

    # navigation from the welcome page 
    def welcome_navigation(self):
        arrow_down = self.browser.find_element(*self.ARROW_DOWN)
        arrow_down.click()

    # open login menu to choose logging user role
    def open_login_menu(self): 
        login_menu_button = self.browser.find_element(*self.LOGIN_MENU_BUTTON)
        login_menu_button.click()

    # clicking at client login form
    def client_login_navigation(self):
        client_login = self.browser.find_element(*self.CLIENT_LOGIN)
        client_login.click()

    def title(self):
        return self.browser.title
    
    