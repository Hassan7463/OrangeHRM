from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LeaveListPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver
    self.leave_list_page_heading = (By.XPATH, "//h5[normalize-space()='Leave List']")

  def get_leave_list_page_heading(self):
    if self.is_displayed(self.leave_list_page_heading):
      return self.get_text(self.leave_list_page_heading)
    else:
      return False
