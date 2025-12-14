from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TimeSheetsPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver
    self.timesheets_heading = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")

  def get_timesheets_page_heading(self):
    if self.is_displayed(self.timesheets_heading):
      return self.get_text(self.timesheets_heading)
    else:
      return False
