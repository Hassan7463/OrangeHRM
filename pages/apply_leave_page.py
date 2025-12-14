from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ApplyLeavePage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver
    self.apply_leave_page_heading = (By.XPATH, "//h6[normalize-space()='Apply Leave']")

  def get_apply_leave_page_heading(self):
    if self.is_displayed(self.apply_leave_page_heading):
      return self.get_text(self.apply_leave_page_heading)
    else:
      return False
