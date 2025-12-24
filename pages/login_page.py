from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver
    self.username_input = (By.NAME, "username")
    self.password_input = (By.NAME, "password")
    self.login_button = (By.XPATH, "//button[normalize-space()='Login']")
    self.login_header = (By.XPATH, "//h5[normalize-space()='Login']")
    self.username_input_required_text = (By.XPATH, "(//*[text() = 'Required'])[1]")
    self.password_input_required_test = (By.XPATH, "(//*[text() = 'Required'])[2]")
    # self.message_invalid_creds = (By.XPATH, "//*[text() = 'Invalid credentials']")
    self.message_invalid_creds = (By.XPATH, "//*[text() = 'Invalid credentials']")

  def opens(self, base_url):
    self.navigate_to(base_url)

  def login(self, username, password):
    self.enter_username(username)
    self.enter_password(password)
    self.click_login()

  def enter_username(self, username):
    self.send_keys(self.username_input, username)

  def enter_password(self, password):
    self.send_keys(self.password_input, password)

  def click_login(self):
    self.click(self.login_button)

  def is_login_heading_displayed(self):
    return self.is_displayed(self.login_header)

  def is_displayed_required_text_for_username(self):
    return self.is_displayed(self.username_input_required_text)

  def is_displayed_required_text_for_password(self):
    return self.is_displayed(self.password_input_required_test)

  def is_invalid_credentials_message_displayed(self):
    return self.is_displayed(self.message_invalid_creds)
