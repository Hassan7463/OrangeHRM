from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AssignLeavePage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver
    self.assign_leave_page_heading = (By.XPATH, "//h6[normalize-space()='Assign Leave']")

  def get_assign_leave_page_heading(self):
    if self.is_displayed(self.assign_leave_page_heading):
      return self.get_text(self.assign_leave_page_heading)
    else:
      return False
