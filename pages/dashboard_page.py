from selenium.webdriver.common.by import By
from pages.base_page import BasePage

search_result = []
class DashboardPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver
    self.dashboard_header = (By.XPATH, "//h6[normalize-space()='Dashboard']")
    self.team_at_work_section_heading = (By.XPATH, "//p[normalize-space()='Time at Work']")
    self.my_actions_section_heading = (By.XPATH, "//p[normalize-space()='My Actions']")
    self.quick_launch_section_heading = (By.XPATH, "//p[normalize-space()='Quick Launch']")
    self.buzz_latest_posts_section_heading = (By.XPATH, "//p[normalize-space()='Buzz Latest Posts']")
    self.employees_on_leave_today_section_heading = (By.XPATH, "//p[normalize-space()='Employees on Leave Today']")
    self.employee_distribution_by_sub_unit_section_heading = (By.XPATH, "//p[normalize-space()='Employee Distribution by Sub Unit']")
    self.employee_distribution_by_location_section_heading = (By.XPATH, "//p[normalize-space()='Employee Distribution by Location']")
    self.assign_leave_image_button = (By.XPATH, "//button[@title='Assign Leave']//*[name()='svg']")
    self.leave_list_image_button = (By.XPATH, "//button[@title='Leave List']//*[name()='svg']")
    self.time_sheets_image_button = (By.XPATH, "//button[@title='Timesheets']//*[name()='svg']")
    self.apply_leave_image_button = (By.XPATH, "//button[@title='Apply Leave']//*[name()='svg']")
    self.my_leave_image_button = (By.XPATH, "//button[@title='My Leave']//*[name()='svg']")
    self.my_timesheet_image_button = (By.XPATH, "//button[@title='My Timesheet']//*[name()='svg']")
    self.search_field_locator = (By.XPATH, "//input[@placeholder='Search']")
    self.filtered_text = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span")

  def is_dashboard_heading_displayed(self):
    return self.is_displayed(self.dashboard_header)

  def is_team_at_work_section_displayed(self):
    return self.is_displayed(self.team_at_work_section_heading)

  def is_my_actions_section_displayed(self):
    return self.is_displayed(self.my_actions_section_heading)

  def is_quick_launch_section_displayed(self):
    return self.is_displayed(self.quick_launch_section_heading)

  def is_buzz_latest_posts_section_displayed(self):
    return self.is_displayed(self.buzz_latest_posts_section_heading)

  def is_employees_on_leave_today_section_displayed(self):
    return self.is_displayed(self.employees_on_leave_today_section_heading)

  def is_employee_distribution_by_sub_unit_section_displayed(self):
    return self.is_displayed(self.employee_distribution_by_sub_unit_section_heading)

  def is_employee_distribution_by_location_section_displayed(self):
    return self.is_displayed(self.employee_distribution_by_location_section_heading)

  def navigate_to_assign_leave_page(self):
    if self.is_displayed(self.assign_leave_image_button) and self.is_enabled(self.leave_list_image_button):
      self.click(self.assign_leave_image_button)
    else:
      print("Assign leave image button is not displayed on dashboard page")

  def navigate_to_leave_list_page(self):
    if self.is_displayed(self.leave_list_image_button) and self.is_enabled(self.leave_list_image_button):
      self.click(self.leave_list_image_button)
    else:
      print("Assign leave image button is not displayed on dashboard page")

  def navigate_to_time_sheets_page(self):
    if self.is_displayed(self.time_sheets_image_button) and self.is_enabled(self.time_sheets_image_button):
      self.click(self.time_sheets_image_button)
    else:
      print("Assign leave image button is not displayed on dashboard page")

  def navigate_to_apply_leave_page(self):
    if self.is_displayed(self.apply_leave_image_button) and self.is_enabled(self.apply_leave_image_button):
      self.click(self.apply_leave_image_button)
    else:
      print("Assign leave image button is not displayed on dashboard page")

  def navigate_to_my_leave_page(self):
    if self.is_displayed(self.my_leave_image_button) and self.is_enabled(self.my_leave_image_button):
      self.click(self.my_leave_image_button)
    else:
      print("Assign leave image button is not displayed on dashboard page")

  def navigate_to_my_timesheet_page(self):
    if self.is_displayed(self.my_timesheet_image_button) and self.is_enabled(self.my_timesheet_image_button):
      self.click(self.my_timesheet_image_button)
    else:
      print("Assign leave image button is not displayed on dashboard page")

  def click_on_search_field(self):
    if self.is_displayed(self.search_field_locator):
      self.click(self.search_field_locator)

  def enter_value_in_search_field(self):
    if self.is_displayed(self.search_field_locator):
      self.send_keys(self.search_field_locator, "p")

  def get_text_after_search(self):
    if self.is_displayed(self.search_field_locator):
      # search_result = [self.filtered_text]
      for item in self.filtered_text:
          result = self.get_text(item)
          search_result.append(result)
  print(search_result)