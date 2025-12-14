from pages.changepassword_page import ChangePasswordPage
from pages.login_page import LoginPage


def test_change_password_page_heading(driver, base_url, credentials, screenshot):
  expected_change_password_page_heading = "Update Password"
  login_page = LoginPage(driver)
  change_password_page = ChangePasswordPage(driver)
  login_page.opens(base_url)
  login_page.login(credentials["username"], credentials["password"])
  change_password_page.navigate_to_change_password_page()
  actual_change_password_page_heading = change_password_page.get_update_password_page_heading()
  assert expected_change_password_page_heading == actual_change_password_page_heading, "Change password page heading is not match!"
