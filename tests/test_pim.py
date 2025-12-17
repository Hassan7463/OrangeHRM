import pytest

from pages.login_page import LoginPage
from pages.menus import Menus
from pages.pim_page import PIM

def test_pim_page_heading(driver, base_url, login_logout):
    expected_pim_page_heading = "PIM"
    menus = Menus(driver)
    pim_page = PIM(driver)
    menus.click_on_pim_menu()
    actual_pim_page_heading = pim_page.get_pim_page_heading()
    assert expected_pim_page_heading == actual_pim_page_heading, "PIM page heading is not displayed!"
