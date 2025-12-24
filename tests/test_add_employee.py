from pages.add_employee_page import AddEmployeePage
from pages.menus import Menus
from pages.pim_page import PIM


def test_add_employee_successfully(driver, login_logout, base_url):
  menus = Menus(driver)
  menus.click_on_pim_menu()
  pim_page = PIM(driver)
  pim_page.click_on_add_button()
  assert pim_page.get_pim_page_heading(), "PIM page heading not displayed!"
  add_employee_page = AddEmployeePage(driver)
  add_employee_page.add_employee_successfully()
