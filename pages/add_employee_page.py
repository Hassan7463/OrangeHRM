from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddEmployeePage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver
    self.add_employee_page_heading = (By.XPATH, "//h6[normalize-space()='Add Employee']")
    self.first_name_field = (By.XPATH, "//input[@placeholder='First Name']")
    self.middle_name_field = (By.XPATH, "//input[@placeholder='Middle Name']")
    self.last_name_field = (By.XPATH, "//input[@placeholder='Last Name']")
    self.employee_id_field = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input")
    self.cancel_button = (By.XPATH, "//button[normalize-space()='Cancel']")
    self.save_button = (By.XPATH, "//button[normalize-space()='Save']")
    self.create_login_details_toggle = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span")
    self.username_label = (By.XPATH, "//*[text() = 'Username']")
    self.username_field = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input")
    self.status_enable_radio_button = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label/span")
    self.status_disable_radio_button = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div/label/span")
    self.password_field = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input")
    self.confirm_password_field = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input")


  def get_employee_page_heading(self):
    actual_add_employee_page_heading = "Add Employee"
    if self.is_displayed(self.add_employee_page_heading):
      expected_add_employee_page_heading = self.get_text(self.add_employee_page_heading)
      if expected_add_employee_page_heading == actual_add_employee_page_heading:
        return True
      else:
        return False
    else:
      return False

  def add_employee_successfully(self):
    self.enter_first_name("Hassan")
    self.enter_middle_name("Ali")
    self.enter_last_name("Khan")
    self.get_employee_id()
    self.click_on_create_login_details_toggle()
    self.enter_user_name("hassana")
    self.check_status_enabled()
    self.enter_password("Hassan123")
    self.enter_confirm_password("Hassan123")
    self.click_on_save()

  def enter_first_name(self, first_name):
    if self.is_displayed(self.first_name_field):
      self.click(self.first_name_field)
      self.send_keys(self.first_name_field, first_name)

  def enter_middle_name(self, middle_name):
    if self.is_displayed(self.middle_name_field):
      self.click(self.middle_name_field)
      self.send_keys(self.middle_name_field, middle_name)

  def enter_last_name(self, last_name):
    if self.is_displayed(self.last_name_field):
      self.click(self.last_name_field)
      self.send_keys(self.last_name_field, last_name)

  def get_employee_id(self):
    if self.is_displayed(self.employee_id_field):
      value = self.__getattribute__(self.employee_id_field)
      emp_id = self.get_text(self.employee_id_field)
      print("employee id is: ",emp_id)

  def click_on_create_login_details_toggle(self):
    username_label = self.is_displayed(self.username_label)
    if not username_label:
      if self.is_displayed(self.create_login_details_toggle):
        self.click(self.create_login_details_toggle)

  def enter_user_name(self, user_name):
    if self.is_displayed(self.username_field):
      self.send_keys(self.username_field, user_name)

  def check_status_enabled(self):
    if self.is_displayed(self.status_enable_radio_button):
      is_enable_status = self.is_selected(self.status_enable_radio_button)
      print("enable status", is_enable_status)
      if not is_enable_status:
        self.click(self.status_enable_radio_button)

  def enter_password(self, password):
    if self.is_displayed(self.password_field):
      self.send_keys(self.password_field, password)

  def enter_confirm_password(self, confirm_password):
    if self.is_displayed(self.confirm_password_field):
      self.send_keys(self.confirm_password_field, confirm_password)

  def click_on_save(self):
    if self.is_displayed(self.save_button):
      self.click(self.save_button)

  def click_on_cancel(self):
    if self.is_displayed(self.cancel_button):
      self.click(self.cancel_button)
