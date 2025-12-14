from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[normalize-space()='Login']")

    def open_browser(self, base_url):
        self.driver.get(base_url)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_on_login_button()

    def enter_username(self, username):
        self.send_keys(self.username_field, username)

    def enter_password(self, password):
        self.send_keys(self.password_field, password)

    def click_on_login_button(self):
        self.click(self.login_button)