from pages.my_timesheet import MyTimesheet
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


def test_my_timesheet_page_heading_displayed(driver, base_url, login_logout):
  expected_my_timesheet_page_heading = "My Timesheet"
  dashboard_page = DashboardPage(driver)
  dashboard_page.navigate_to_my_timesheet_page()
  my_timesheet_page = MyTimesheet(driver)
  actual_my_timesheet_page_heading = my_timesheet_page.get_my_timesheet_page_heading()
  assert expected_my_timesheet_page_heading == actual_my_timesheet_page_heading, "My timesheet page heading is not displayed on the page!"
