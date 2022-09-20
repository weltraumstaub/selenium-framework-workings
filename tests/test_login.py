"""
Login Page Test    
"""
import pytest

from pages.main_page import MainPage
from pages.client_login_page import ClientLoginPage

def test_client_login_navigation(browser):
  main_page = MainPage(browser)
  login_page = ClientLoginPage(browser)

  # Given the site page is loaded 
  main_page.load()
  
  # Then user accept cookie policy 
  main_page.accept_cookies()
  
  # Then user navigates away from the welcome screen to the second section of the landing
  main_page.welcome_navigation()

  # Then user clicks at the menu button in header to choose login form 
  main_page.open_login_menu()

  # Then user clicks at the client login link in the navigation bar 
  main_page.client_login_navigation()

  assert main_page.title() == "Грань"
  
  # Then user accept site policy in the login form 
  login_page.accept_site_policy() 

  # Then user enters phone number into the field 
  login_page.input_phone_number()

  # Then user click on the login button 
  login_page.click_login_button()

  assert browser.current_url == "https://stage.psyedge.ru/Client/RegistrationSmsPage"