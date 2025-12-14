from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage

class LogoutPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver
    self.user_dropdown_header = (By.XPATH, "//p[@class='oxd-userdropdown-name']") # Ask
    self.logout_header_menu = (By.XPATH, "//a[normalize-space()='Logout']")

  def navigate_to_logout(self):
    if self.is_displayed(self.user_dropdown_header):
      self.click(self.user_dropdown_header)

    if self.is_enabled(self.logout_header_menu):
      self.click(self.logout_header_menu)
