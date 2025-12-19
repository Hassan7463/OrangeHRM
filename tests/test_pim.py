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

def test_verify_searched_record_not_listed(driver, base_url, login_logout):
  menus = Menus(driver)
  pim_page = PIM(driver)
  menus.click_on_pim_menu()
  pim_page.enter_value_in_employee_name_field()
  assert pim_page.verify_searched_record_not_listed()

def test_verify_searched_record_not_in_table(driver, base_url, login_logout):
  menus = Menus(driver)
  pim_page = PIM(driver)
  menus.click_on_pim_menu()
  pim_page.enter_value_in_employee_name_field()
  pim_page.click_on_search_button()
  assert pim_page.verify_searched_record_not_in_table()

def test_verify_functionality_of_reset_button(driver, base_url, login_logout):
  menus = Menus(driver)
  pim_page = PIM(driver)
  menus.click_on_pim_menu()
  pim_page.enter_value_in_employee_name_field()
  pim_page.click_on_search_button()
  pim_page.click_on_reset_button()
  assert pim_page.verify_records_listed_in_table_on_reset()
