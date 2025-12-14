from pages.my_timesheet import MyTimesheet
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


def test_my_timesheet_page_heading_displayed(driver, base_url, credentials):
  expected_my_timesheet_page_heading = "My Timesheet"
  login_page = LoginPage(driver)
  dashboard_page = DashboardPage(driver)
  login_page.opens(base_url)
  login_page.login(credentials["username"], credentials["password"])
  dashboard_page.navigate_to_my_timesheet_page()
  my_timesheet_page = MyTimesheet(driver)
  actual_my_timesheet_page_heading = my_timesheet_page.get_my_timesheet_page_heading()
  assert expected_my_timesheet_page_heading == actual_my_timesheet_page_heading, "My timesheet page heading is not displayed on the page!"
