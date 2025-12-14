from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SupportPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver
    self.user_dropdown_header = (By.XPATH, "//p[@class='oxd-userdropdown-name']") # Ask
    self.support_header_menu = (By.XPATH, "//a[normalize-space()='Support']")
    self.support_page_heading = (By.XPATH, "//h6[normalize-space()='Getting Started with OrangeHRM']")

  def navigate_to_support_page(self):
    if self.is_displayed(self.user_dropdown_header):
      self.click(self.user_dropdown_header)

    if self.is_enabled(self.support_header_menu):
      self.click(self.support_header_menu)

  def get_support_page_heading(self):
    check = self.get_text(self.support_page_heading)
    print(check)
    return check