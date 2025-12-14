from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MyLeavePage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver
    self.my_leave_page_heading = (By.XPATH, "//a[normalize-space()='My Leave']")

  def get_my_leave_page_heading(self):
    if self.is_displayed(self.my_leave_page_heading):
      return self.get_text(self.my_leave_page_heading)
    else:
      return False
