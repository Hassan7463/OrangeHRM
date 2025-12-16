from pages.time_sheets_page import TimeSheetsPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


def test_timesheets_page_heading_displayed(driver, base_url, login_logout):
  expected_timesheet_page_heading = "Time"
  dashboard_page = DashboardPage(driver)
  dashboard_page.navigate_to_time_sheets_page()
  timesheets_page = TimeSheetsPage(driver)
  actual_timesheet_page_heading = timesheets_page.get_timesheets_page_heading()
  assert expected_timesheet_page_heading == actual_timesheet_page_heading, "Timesheet page heading is not displayed on the page!"
