from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class PIM(BasePage):
    def __init__(self, driver):
      super().__init__(driver)
      self.driver = driver
      self.pim_page_heading = (By.XPATH, "//h6[normalize-space()='PIM']")
      self.employee_information_heading = (By.XPATH, "//h5[normalize-space()='Employee Information']")
      self.add_employee_button = (By.XPATH, "//button[normalize-space()='Add']")
      self.reset_button = (By.XPATH, "//button[normalize-space()='Reset']")
      self.search_button = (By.XPATH, "//button[normalize-space()='Search']")
      # Employee Information section
      self.employee_name_field = (By.XPATH, "//div[@class='oxd-autocomplete-text-input oxd-autocomplete-text-input--focus']")
      self.no_records_found_for_listbox = (By.XPATH, "//div[@role='option']")
      self.no_records_found_for_table = (By.XPATH, "//span[normalize-space()='No Records Found']")
      self.message_records_found = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span")

    def get_pim_page_heading(self):
      if self.is_displayed(self.pim_page_heading):
        return self.get_text(self.pim_page_heading)
      else:
        return False

    def get_employee_information_heading(self):
      if self.is_displayed(self.employee_information_heading):
        return self.get_text(self.employee_information_heading)
      else:
        return False

    def click_on_add_button(self):
      if self.is_displayed(self.add_employee_button):
        self.click(self.add_employee_button)

    def click_on_search_button(self):
      if self.is_displayed(self.search_button):
        self.click(self.search_button)

    def click_on_reset_button(self):
      if self.is_displayed(self.reset_button):
        self.click(self.reset_button)

    def enter_value_in_employee_name_field(self):
      if self.is_displayed(self.employee_name_field):
        self.click(self.employee_name_field)
        self.send_keys(self.employee_name_field, "Hassan Ali Khan")

    def verify_searched_record_not_listed(self):
      actual_message = "No Records Found"
      if self.is_displayed(self.no_records_found_for_listbox):
        expected_message = self.get_text(self.no_records_found_for_listbox)
        if expected_message == actual_message:
          return True
        else:
          return False
      else:
        return "User has searched in the list"

    def verify_searched_record_not_in_table(self):
      actual_message = "No Records Found"
      if self.is_displayed(self.no_records_found_for_table):
        expected_message = self.get_text(self.no_records_found_for_table)
        if expected_message == actual_message:
          return True
        else:
          return False
      else:
        return "Searched record not available in the table"

    def verify_records_listed_in_table_on_reset(self):
      expected_message = "No Records Found"
      if self.is_displayed(self.message_records_found):
        actual_message = self.get_text(self.message_records_found)
        if expected_message != actual_message:
          return True
        else:
          return False
      else:
        return "On reset, records not listed in the table"

    def add_employee_successfully(self):
      if self.is_displayed(self.employee_information_heading):
        return self.get_text(self.employee_information_heading)
      else:
        return False
