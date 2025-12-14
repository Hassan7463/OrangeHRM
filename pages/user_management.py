from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UserManagementPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.add_user_heading = (By.XPATH, "//h6[normalize-space()='Add User']")
    self.save_button = (By.XPATH, "//button[normalize-space()='Save']")
    self.required_text_for_user_role_dropdown = (By.XPATH, "//div[@class='oxd-form-row']//div[@class='oxd-grid-2 orangehrm-full-width-grid']//div[1]//div[1]//span[1]")
    self.required_text_for_employee_name_field = (By.XPATH, "//div[@class='oxd-form-row']//div[2]//div[1]//span[1]")
    self.required_text_for_status_dropdown = (By.XPATH, "//div[3]//div[1]//span[1]")
    self.required_text_for_username_field = (By.XPATH, "//div[4]//div[1]//span[1]")
    self.required_text_for_password_field = (By.XPATH, "//div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message'][normalize-space()='Required']")
    self.user_role_dropdown = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div")
    self.employee_name_field = (By.XPATH, "//input[@placeholder='Type for hints...']")
    self.status_dropdown = (By.XPATH, "//div[3]//div[1]//div[2]//div[1]//div[1]//div[1]")
    self.user_name_field = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input")
    self.password_field = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input")
    self.confirm_password_field = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input")
    self.required_text_for_confirm_password_field = (By.XPATH, "")
    self.user_role_dd_value_admin = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]/span")
    self.status_dd_value_enabled = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]/span")
    self.employee_name_field_autocomplete_value = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div/span")
    self.username_locater = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]")

  def get_add_user_page_heading(self):
    if self.is_displayed(self.add_user_heading):
      return self.get_text(self.add_user_heading)
    else:
      return False

  def click_on_save_button(self):
    if self.is_displayed(self.save_button):
      self.click(self.save_button)

  def check_required_message_for_mandatory_field(self):
    if ((self.is_displayed(self.required_text_for_user_role_dropdown)) and
      (self.is_displayed(self.required_text_for_employee_name_field)) and
      (self.is_displayed(self.required_text_for_status_dropdown)) and
      (self.is_displayed(self.required_text_for_username_field)) and
      (self.is_displayed(self.required_text_for_password_field))):
      return True
    else:
      return False

  def add_user_successfully(self):
    if self.is_displayed(self.user_role_dropdown):
      self.click(self.user_role_dropdown)
      if self.is_displayed(self.user_role_dd_value_admin):
        self.click(self.user_role_dd_value_admin)

    if self.is_displayed(self.employee_name_field):
      self.click(self.employee_name_field)
      self.send_keys(self.employee_name_field, "Thomas Kutty Benny")
      if self.is_displayed(self.employee_name_field_autocomplete_value):
        self.click(self.employee_name_field_autocomplete_value)

    if self.is_displayed(self.status_dropdown):
      self.click(self.status_dropdown)
      if self.is_displayed(self.status_dd_value_enabled):
        self.click(self.status_dd_value_enabled)

    if self.is_displayed(self.user_name_field):
      self.click(self.user_name_field)
      self.send_keys(self.user_name_field, "hassana")

    if self.is_displayed(self.password_field):
      self.click(self.password_field)
      self.send_keys(self.password_field, "admin123")

    if self.is_displayed(self.confirm_password_field):
      self.click(self.confirm_password_field)
      self.send_keys(self.confirm_password_field, "admin123")

  def edit_user_successfully(self):
    if self.is_displayed(self.username_locater):
      self.get_text(self.username_locater)

  def delete_user_successfully(self):
    if self.is_displayed(self.add_user_heading):
      self.click(self.add_user_heading)
