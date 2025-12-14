from pages.my_leave_page import MyLeavePage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


def test_my_leave_page_heading_displayed(driver, base_url, credentials):
  expected_my_leave_page_heading = "My Leave"
  login_page = LoginPage(driver)
  dashboard_page = DashboardPage(driver)
  login_page.opens(base_url)
  login_page.login(credentials["username"], credentials["password"])
  dashboard_page.navigate_to_my_leave_page()
  my_leave_page = MyLeavePage(driver)
  actual_my_leave_page_heading = my_leave_page.get_my_leave_page_heading()
  assert expected_my_leave_page_heading == actual_my_leave_page_heading, "My leave page heading is not displayed on the page!"
