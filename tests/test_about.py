import time

import pytest

from pages.login_page import LoginPage
from pages.About import AboutPage

@pytest.mark.skip(reason="skip test due to unable to locate about popup heading")
def test_about_popup_heading(driver, base_url, credentials, screenshot):
  expected_about_popup_heading = "About"
  login_page = LoginPage(driver)
  about_page = AboutPage(driver)
  login_page.opens(base_url)
  login_page.login(credentials["username"], credentials["password"])
  about_page.navigate_to_about_page()
  actual_about_popup_heading = about_page.about_popup_heading
  assert expected_about_popup_heading == actual_about_popup_heading, "About popup heading is not displayed!"
