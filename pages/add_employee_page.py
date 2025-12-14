from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddEmployeePage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver
    self.add_employee_page_heading = (By.XPATH, "//h6[normalize-space()='Add Employee']")
    self.first_name_field = (By.XPATH, "//input[@placeholder='First Name']")
    self.middle_name_field = (By.XPATH, "//input[@placeholder='Middle Name']")
    self.last_name_field = (By.XPATH, "//input[@placeholder='Last Name']")
    self.employee_id_field = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input")
    self.cancel_button = (By.XPATH, "//button[normalize-space()='Cancel']")
    self.save_button = (By.XPATH, "//button[normalize-space()='Save']")

  def get_employee_page_heading(self):
    actual_add_employee_page_heading = "Add Employee"
    if self.is_displayed(self.add_employee_page_heading):
      expected_add_employee_page_heading = self.get_text(self.add_employee_page_heading)
      if expected_add_employee_page_heading == actual_add_employee_page_heading:
        return True
      else:
        return False
    else:
      return False

  def add_employee_successfully(self):
    if self.is_displayed(self.first_name_field):
      self.click(self.first_name_field)
      self.send_keys(self.first_name_field, "Hassan")

    if self.is_displayed(self.middle_name_field):
      self.click(self.middle_name_field)
      self.send_keys(self.middle_name_field, "Ali")

    if self.is_displayed(self.last_name_field):
      self.click(self.last_name_field)
      self.send_keys(self.last_name_field, "Khan")

    if self.is_displayed(self.employee_id_field):
      self.click(self.employee_id_field)
      self.send_keys(self.employee_id_field, "2381")
