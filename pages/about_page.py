from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AboutPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver
    self.user_dropdown_header = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    self.about_header_menu = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[1]/a")
    self.about_popup_heading = (By.XPATH, "//h6[contains(@class,'orangehrm-main-title')]")

  def navigate_to_about_page(self):
    print("Hassan")
    if self.is_displayed(self.user_dropdown_header):
      self.click(self.user_dropdown_header)

    if self.is_displayed(self.about_header_menu):
      self.click(self.about_header_menu)
    print("Ali")


  def about_popup_title(self):
    # print(self.driver.page_source)
    # self.driver.switch_to.frame(0)
    print("Khan")
    if self.is_displayed(self.about_popup_heading):
      check = self.get_text(self.about_popup_heading)
      print("About popup title:", check)
      return check
    else:
      return False
