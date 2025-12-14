from pages.time_sheets_page import TimeSheetsPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


def test_timesheets_page_heading_displayed(driver, base_url, credentials):
  expected_timesheet_page_heading = "Time"
  login_page = LoginPage(driver)
  dashboard_page = DashboardPage(driver)
  login_page.opens(base_url)
  login_page.login(credentials["username"], credentials["password"])
  dashboard_page.navigate_to_time_sheets_page()
  timesheets_page = TimeSheetsPage(driver)
  actual_timesheet_page_heading = timesheets_page.get_timesheets_page_heading()
  assert expected_timesheet_page_heading == actual_timesheet_page_heading, "Timesheet page heading is not displayed on the page!"
