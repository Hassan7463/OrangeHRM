import time

from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from pages.user_management import UserManagementPage
from pages.menus import Menus

def test_add_user_page_heading(driver, base_url, login_logout):
  expected_add_user_page_heading = "Add User"
  menus = Menus(driver)
  menus.click_on_admin_menu()
  admin_page = AdminPage(driver)
  admin_page.click_on_add_user_button()
  add_user_page = UserManagementPage(driver)
  actual_add_user_page_heading = add_user_page.get_add_user_page_heading()
  assert expected_add_user_page_heading == actual_add_user_page_heading, "Add user page heading in not displayed!"

def test_empty_field_validations_for_add_user_page(driver, base_url, login_logout):
  menus = Menus(driver)
  menus.click_on_admin_menu()
  admin_page = AdminPage(driver)
  admin_page.click_on_add_user_button()
  add_user_page = UserManagementPage(driver)
  add_user_page.click_on_save_button()
  assert add_user_page.check_required_message_for_mandatory_field()

def test_add_user_successfully(driver, base_url, login_logout):
  menus = Menus(driver)
  menus.click_on_admin_menu()
  admin_page = AdminPage(driver)
  admin_page.click_on_add_user_button()
  add_user_page = UserManagementPage(driver)
  add_user_page.add_user_successfully()
  time.sleep(5)
