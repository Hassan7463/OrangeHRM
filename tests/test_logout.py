from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.logout_page import LogoutPage

def test_logout(driver, base_url, login_logout):
  login_page = LoginPage(driver)
  logout_page = LogoutPage(driver)
  logout_page.logout()
  assert login_page.is_login_heading_displayed(), "Application is not logging out and Login page heading is not displayed"
