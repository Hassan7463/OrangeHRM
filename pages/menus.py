from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Menus(BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.menu_admin = (By.XPATH, "//span[normalize-space()='Admin']")
    self.menu_pim = (By.XPATH, "//span[normalize-space()='PIM']")
    self.menu_leave = (By.XPATH, "//span[normalize-space()='Leave']")
    self.menu_time = (By.XPATH, "//span[normalize-space()='Time']")
    self.menu_recruitment = (By.XPATH, "//span[normalize-space()='Recruitment']")
    self.menu_my_info = (By.XPATH, "//span[normalize-space()='My Info']")
    self.menu_performance = (By.XPATH, "//span[normalize-space()='My Info']")
    self.menu_dashboard = (By.XPATH, "//span[normalize-space()='Dashboard']")
    self.menu_directory = (By.XPATH, "//span[normalize-space()='Directory']")
    self.menu_maintenance = (By.XPATH, "//span[normalize-space()='Maintenance']")
    self.menu_claim = (By.XPATH, "//span[normalize-space()='Claim']")
    self.menu_buzz = (By.XPATH, "//span[normalize-space()='Buzz']")

  def click_on_admin_menu(self):
    if self.is_displayed(self.menu_admin):
      self.click(self.menu_admin)

  def click_on_pim_menu(self):
    if self.is_displayed(self.menu_pim):
      self.click(self.menu_pim)

  def click_on_leave_menu(self):
    if self.is_displayed(self.menu_leave):
      self.click(self.menu_leave)

  def click_on_time_menu(self):
    if self.is_displayed(self.menu_time):
      self.click(self.menu_time)

  def click_on_recruitment_menu(self):
    if self.is_displayed(self.menu_recruitment):
      self.click(self.menu_recruitment)

  def click_on_my_info_menu(self):
    if self.is_displayed(self.menu_my_info):
      self.click(self.menu_my_info)

  def click_on_performance_menu(self):
    if self.is_displayed(self.menu_performance):
      self.click(self.menu_performance)

  def click_on_dashboard_menu(self):
    if self.is_displayed(self.menu_dashboard):
      self.click(self.menu_dashboard)

  def click_on_directory_menu(self):
    if self.is_displayed(self.menu_directory):
      self.click(self.menu_directory)

  def click_on_maintenance_menu(self):
    if self.is_displayed(self.menu_maintenance):
      self.click(self.menu_maintenance)

  def click_on_claim_menu(self):
    if self.is_displayed(self.menu_claim):
      self.click(self.menu_claim)

  def click_on_buzz_menu(self):
    if self.is_displayed(self.menu_buzz):
      self.click(self.menu_buzz)
