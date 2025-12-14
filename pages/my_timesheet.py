from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MyTimesheet(BasePage):
    def __init__(self, driver):
      super().__init__(driver)
      self.driver = driver
      self.my_timesheet_page_heading = (By.XPATH, "//h6[normalize-space()='My Timesheet']")

    def get_my_timesheet_page_heading(self):
      if self.is_displayed(self.my_timesheet_page_heading):
        return self.get_text(self.my_timesheet_page_heading)
      else:
        return False
