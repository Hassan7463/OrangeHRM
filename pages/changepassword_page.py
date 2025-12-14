from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ChangePasswordPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver
    self.user_dropdown_header = (By.XPATH, "//p[@class='oxd-userdropdown-name']") # Ask
    self.change_password_header_menu = (By.XPATH, "//a[normalize-space()='Change Password']")
    self.update_password_page_heading = (By.XPATH, "//h6[normalize-space()='Update Password']")

  def navigate_to_change_password_page(self):
    if self.is_displayed(self.user_dropdown_header):
      self.click(self.user_dropdown_header)

    if self.is_enabled(self.change_password_header_menu):
      self.click(self.change_password_header_menu)

  def get_update_password_page_heading(self):
    if self.is_displayed(self.update_password_page_heading):
      check = self.get_text(self.update_password_page_heading)
      print(check)
      return check
    return None
