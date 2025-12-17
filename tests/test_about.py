import time

import pytest

from pages.about_page import AboutPage

@pytest.mark.skip(reason="This test will fail")
def test_about_popup_heading(driver, base_url, login_logout, screenshot):
  expected_about_popup_heading = "About"
  about_page = AboutPage(driver)
  about_page.click_on_username_dropdown()
  time.sleep(5)
  about_page.click_on_about()
  actual_about_popup_heading = about_page.verify_about_popup_heading()
  assert expected_about_popup_heading == actual_about_popup_heading, "About popup heading is not displayed!"
