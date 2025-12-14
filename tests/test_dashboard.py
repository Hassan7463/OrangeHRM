from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
import time

def test_dashboard_page_heading_displayed(driver, base_url, credentials, screenshot):
  login_page = LoginPage(driver)
  dashboard_page = DashboardPage(driver)
  login_page.opens(base_url)
  login_page.login(credentials["username"], credentials["password"])
  dashboard_page.is_dashboard_heading_displayed()
  assert dashboard_page.is_dashboard_heading_displayed(), "Dashboard Heading is not displayed"

def test_team_at_work_section_displayed(driver, base_url, credentials):
  login_page = LoginPage(driver)
  dashboard_page = DashboardPage(driver)
  login_page.opens(base_url)
  login_page.login(credentials["username"], credentials["password"])
  assert dashboard_page.is_team_at_work_section_displayed(), "Team work section heading is not displayed"

def test_my_actions_section_displayed(driver, base_url, credentials):
  login_page = LoginPage(driver)
  dashboard_page = DashboardPage(driver)
  login_page.opens(base_url)
  login_page.login(credentials["username"], credentials["password"])
  assert dashboard_page.is_my_actions_section_displayed(), "My actions section heading is not displayed"

def test_quick_launch_section_displayed(driver, base_url, credentials):
  login_page = LoginPage(driver)
  dashboard_page = DashboardPage(driver)
  login_page.opens(base_url)
  login_page.login(credentials["username"], credentials["password"])
  assert dashboard_page.is_quick_launch_section_displayed(), "Quick launch section heading is not displayed"

def test_buzz_latest_posts_section_displayed(driver, base_url, credentials):
  login_page = LoginPage(driver)
  dashboard_page = DashboardPage(driver)
  login_page.opens(base_url)
  login_page.login(credentials["username"], credentials["password"])
  assert dashboard_page.is_buzz_latest_posts_section_displayed(), "Buzz latest posts section is not displayed"

def test_employees_on_leave_today_section_displayed(driver, base_url, credentials):
  login_page = LoginPage(driver)
  dashboard_page = DashboardPage(driver)
  login_page.opens(base_url)
  login_page.login(credentials["username"], credentials["password"])
  assert dashboard_page.is_employees_on_leave_today_section_displayed(), "Employee on leave today section heading is not displayed"

def test_employee_distribution_by_sub_unit_section_displayed(driver, base_url, credentials):
  login_page = LoginPage(driver)
  dashboard_page = DashboardPage(driver)
  login_page.opens(base_url)
  login_page.login(credentials["username"], credentials["password"])
  assert dashboard_page.is_employee_distribution_by_sub_unit_section_displayed(), "Employee distribution by sub unit section heading is not displayed"

def test_employee_distribution_by_location_section_displayed(driver, base_url, credentials):
  login_page = LoginPage(driver)
  dashboard_page = DashboardPage(driver)
  login_page.opens(base_url)
  login_page.login(credentials["username"], credentials["password"])
  assert dashboard_page.is_employee_distribution_by_location_section_displayed(), "Employee distribution by location heading is not displayed"

def test_search_result_displayed(driver, base_url, credentials, screenshot):
  login_page = LoginPage(driver)
  dashboard_page = DashboardPage(driver)
  login_page.opens(base_url)
  login_page.login(credentials["username"], credentials["password"])
  dashboard_page.click_on_search_field()
  dashboard_page.enter_value_in_search_field()
  time.sleep(5)
  dashboard_page.get_text_after_search()
  # assert dashboard_page.is_employee_distribution_by_location_section_displayed(), "Employee distribution by location heading is not displayed"