from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from pages.menus import Menus


def test_admin_page_heading(driver, base_url, credentials):
  expected_admin_page_heading = "Admin"
  login_page = LoginPage(driver)
  menus = Menus(driver)
  admin_page = AdminPage(driver)
  login_page.opens(base_url)
  login_page.login(credentials["username"], credentials["password"])
  menus.click_on_admin_menu()
  actual_admin_page_heading = admin_page.get_admin_page_heading()
  assert expected_admin_page_heading == actual_admin_page_heading, "Admin page heading is not displayed!"
