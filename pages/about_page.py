from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AboutPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver
    self.user_dropdown_header = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    self.about_header_menu = (By.XPATH, "//a[text()='About']")
    self.about_popup_heading = (By.XPATH, "//h6[text()='About']")
    # self.about_popup_heading = (By.XPATH, "//h6[normalize-space()='About']")

  def click_on_username_dropdown(self):
    print("0ne")
    if self.is_displayed(self.user_dropdown_header):
      self.click(self.user_dropdown_header)

  def click_on_about(self):
    print("Two")
    if self.is_displayed(self.about_header_menu):
      self.click(self.about_header_menu)

  def verify_about_popup_heading(self):
    if self.is_displayed(self.about_popup_heading):
      popup_heading = self.get_text(self.about_popup_heading)
      print("popup heading is:", popup_heading)
      return popup_heading
    else:
      return False
