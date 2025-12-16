from pages.my_leave_page import MyLeavePage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


def test_my_leave_page_heading_displayed(driver, base_url, login_logout):
  expected_my_leave_page_heading = "My Leave"
  dashboard_page = DashboardPage(driver)
  dashboard_page.navigate_to_my_leave_page()
  my_leave_page = MyLeavePage(driver)
  actual_my_leave_page_heading = my_leave_page.get_my_leave_page_heading()
  assert expected_my_leave_page_heading == actual_my_leave_page_heading, "My leave page heading is not displayed on the page!"
