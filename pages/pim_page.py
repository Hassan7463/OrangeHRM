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

    def add_employee_successfully(self):
      if self.is_displayed(self.employee_information_heading):
        return self.get_text(self.employee_information_heading)
      else:
        return False
