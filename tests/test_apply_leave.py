from pages.apply_leave_page import ApplyLeavePage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


def test_apply_leave_page_heading_displayed(driver, base_url, credentials):
  expected_apply_leave_page_heading = "Apply Leave"
  login_page = LoginPage(driver)
  dashboard_page = DashboardPage(driver)
  login_page.opens(base_url)
  login_page.login(credentials["username"], credentials["password"])
  dashboard_page.navigate_to_apply_leave_page()
  apply_leave_page = ApplyLeavePage(driver)
  actual_apply_leave_page_heading = apply_leave_page.get_apply_leave_page_heading()
  assert expected_apply_leave_page_heading == actual_apply_leave_page_heading, "Apply leave page heading is not displayed on the page!"
