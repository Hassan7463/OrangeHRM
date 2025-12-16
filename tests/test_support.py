from pages.login_page import LoginPage
from pages.support_page import SupportPage

def test_about_popup_heading(driver, base_url, login_logout):
  expected_support_page_heading = "Getting Started with OrangeHRM"
  support_page = SupportPage(driver)
  support_page.navigate_to_support_page()
  actual_support_page_heading = support_page.get_support_page_heading()
  assert expected_support_page_heading == actual_support_page_heading, "Support page heading is not displayed!"
