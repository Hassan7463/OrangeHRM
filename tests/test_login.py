import time

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

def test_verify_login_page_heading(driver, base_url, screenshot):
  login_page = LoginPage(driver)
  login_page.opens(base_url)
  assert login_page.is_login_heading_displayed(), "Login page heading is not displayed"

def test_login_with_empty_credentials(driver, base_url):
  login_page = LoginPage(driver)
  login_page.opens(base_url)
  login_page.login("", "")
  assert login_page.is_displayed_required_text_for_username(), "Username field is not required."
  assert login_page.is_displayed_required_text_for_password(), "Password field is not required."

def test_login_with_invalid_credentials(driver, base_url):
    login_page = LoginPage(driver)
    login_page.opens(base_url)
    login_page.login("admin", "admin")
    assert login_page.is_invalid_credentials_message_displayed(), "Credentials are invalid."

def test_login_with_valid_credentials(driver, base_url, login_logout):
  dashboard_page = DashboardPage(driver)
  assert dashboard_page.is_dashboard_heading_displayed(), "Dashboard Heading is not displayed"
  assert dashboard_page.is_team_at_work_section_displayed(), "Team at Work section is not displayed"
