import time

from pages.login_page import LoginPage

def test_login_valid_credentials(driver, base_url,credentials):
    login_page = LoginPage(driver)
    login_page.open_browser(    base_url)
    time.sleep(5)
    login_page.login(credentials["username"], credentials["password"])
