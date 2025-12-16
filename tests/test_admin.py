from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from pages.menus import Menus


def test_admin_page_heading(driver, base_url, login_logout):
  expected_admin_page_heading = "Admin"
  menus = Menus(driver)
  admin_page = AdminPage(driver)
  menus.click_on_admin_menu()
  actual_admin_page_heading = admin_page.get_admin_page_heading()
  assert expected_admin_page_heading == actual_admin_page_heading, "Admin page heading is not displayed!"
