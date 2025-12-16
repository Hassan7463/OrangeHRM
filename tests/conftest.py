from selenium import webdriver
import pytest
import os
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from utils.screenshot_utility import ScreenshotUtility
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from selenium.common.exceptions import NoSuchElementException

load_dotenv()

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("headless")
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    return os.getenv("BASE_URL")

@pytest.fixture
def credentials():
    return {
        "username": os.getenv("APP_USERNAME"),
        "password": os.getenv("APP_PASSWORD")
    }

@pytest.fixture()
def screenshot(driver, request):
    screenshot_util = ScreenshotUtility(driver)
    yield screenshot_util

    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        test_name = request.node.nodeid
        error_message = "Test Failed"

        if hasattr(request.node.rep_call, 'longrepr'):
            error_str = str(request.node.rep_call.longrepr)

            if "AssertionError:" in error_str:
                error_message = (
                    error_str.split("AssertionError:")[-1].strip().split('\n')[0]
                )

            elif error_str:
                lines = error_str.split('\n')
                for line in lines:
                    if line.strip() and not line.startswith('E ') and len(line.strip()) > 10:
                        error_message = line.strip()
                        break

        screenshot_util.take_failure_screenshot(test_name, error_message)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture()
def login_logout(driver, base_url, credentials):
  login_page = LoginPage(driver)
  logout_page = LogoutPage(driver)
  login_page.opens(base_url)
  login_page.login(credentials["username"], credentials["password"])
  yield login_page
  try:
    logout_page.logout()
  except NoSuchElementException:
    pass
