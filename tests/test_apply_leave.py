from pages.apply_leave_page import ApplyLeavePage
from pages.dashboard_page import DashboardPage

def test_apply_leave_page_heading_displayed(driver, base_url, login_logout):
  expected_apply_leave_page_heading = "Apply Leave"
  dashboard_page = DashboardPage(driver)
  dashboard_page.navigate_to_apply_leave_page()
  apply_leave_page = ApplyLeavePage(driver)
  actual_apply_leave_page_heading = apply_leave_page.get_apply_leave_page_heading()
  assert expected_apply_leave_page_heading == actual_apply_leave_page_heading, "Apply leave page heading is not displayed on the page!"
