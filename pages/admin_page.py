from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AdminPage(BasePage):
    def __init__(self, driver):
      super().__init__(driver)
      self.driver = driver
      self.admin_page_heading = (By.XPATH, "//h6[normalize-space()='Admin']")
      self.add_user_button = (By.XPATH, "//button[normalize-space()='Add']")

    def get_admin_page_heading(self):
      if self.is_displayed(self.admin_page_heading):
        return self.get_text(self.admin_page_heading)
      else:
        return False

    def click_on_add_user_button(self):
      if self.is_displayed(self.add_user_button):
        self.click(self.add_user_button)
      else:
        print("Add user button not displayed")
