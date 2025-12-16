from pages.assign_leave_page import AssignLeavePage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


def test_assign_leave_page_heading_displayed(driver, base_url, login_logout):
  expected_assign_leave_page_heading = "Assign Leave"
  dashboard_page = DashboardPage(driver)
  dashboard_page.navigate_to_assign_leave_page()
  assign_leave_page = AssignLeavePage(driver)
  actual_assign_leave_page_heading = assign_leave_page.get_assign_leave_page_heading()
  assert expected_assign_leave_page_heading == actual_assign_leave_page_heading, "Assign leave page heading is not displayed on the page!"
