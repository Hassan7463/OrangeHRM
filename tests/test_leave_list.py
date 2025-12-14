from pages.leave_list_page import LeaveListPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.menus import Menus

expected_leave_list_page_heading = "Leave List"
def test_leave_list_page_heading_displayed_from_dashboard(driver, base_url, credentials):
  login_page = LoginPage(driver)
  dashboard_page = DashboardPage(driver)
  login_page.opens(base_url)
  login_page.login(credentials["username"], credentials["password"])
  dashboard_page.navigate_to_leave_list_page()
  leave_list_page = LeaveListPage(driver)
  actual_leave_list_page_heading = leave_list_page.get_leave_list_page_heading()
  assert expected_leave_list_page_heading == actual_leave_list_page_heading, "Leave list page heading is not displayed from the dashboard!"

def test_leave_list_page_heading_displayed_from_menu(driver, base_url, credentials):
  login_page = LoginPage(driver)
  login_page.opens(base_url)
  menu_page = Menus(driver)
  leave_list_page = LeaveListPage(driver)
  login_page.login(credentials["username"], credentials["password"])
  menu_page.click_on_leave_menu()
  actual_leave_list_page_heading = leave_list_page.get_leave_list_page_heading()
  assert expected_leave_list_page_heading == actual_leave_list_page_heading, "Leave list page heading is not displayed from the menu!"
