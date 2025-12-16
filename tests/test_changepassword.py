from pages.changepassword_page import ChangePasswordPage
from pages.login_page import LoginPage


def test_change_password_page_heading(driver, base_url, login_logout):
  expected_change_password_page_heading = "Update Password"
  change_password_page = ChangePasswordPage(driver)
  change_password_page.navigate_to_change_password_page()
  actual_change_password_page_heading = change_password_page.get_update_password_page_heading()
  assert expected_change_password_page_heading == actual_change_password_page_heading, "Change password page heading is not match!"
