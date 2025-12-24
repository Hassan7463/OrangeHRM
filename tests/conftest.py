import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common.exceptions import NoSuchElementException
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from utils.screenshot_utility import ScreenshotUtility
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

# Load environment variables
load_dotenv()


# --------------------------
# Pytest CLI option for browser
# --------------------------
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome / firefox / edge"
    )


# --------------------------
# WebDriver fixture
# --------------------------
@pytest.fixture
def driver(pytestconfig):
    browser = pytestconfig.getoption("--browser").lower()

    if browser == "chrome":
        # chrome_options = ChromeOptions()
        # chrome_options.add_argument("--headless")   # remove if you want visible browser
        # driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome()

    elif browser == "firefox":
        import tempfile
        firefox_options = FirefoxOptions()
        # firefox_options.add_argument("--headless")
        firefox_options.binary_location = "/usr/bin/firefox"

        profile_path = tempfile.mkdtemp()
        firefox_options.add_argument("-profile")
        firefox_options.add_argument(profile_path)

        driver = webdriver.Firefox(options=firefox_options)

    elif browser == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--headless")
        driver = webdriver.Edge(options=edge_options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()


# --------------------------
# Base URL fixture
# --------------------------
@pytest.fixture
def base_url():
    return os.getenv("BASE_URL")


# --------------------------
# Credentials fixture
# --------------------------
@pytest.fixture
def credentials():
    return {
        "username": os.getenv("APP_USERNAME"),
        "password": os.getenv("APP_PASSWORD")
    }


# --------------------------
# Screenshot fixture
# --------------------------
@pytest.fixture()
def screenshot(driver, request):
    screenshot_util = ScreenshotUtility(driver)
    yield screenshot_util

    # Capture screenshot on test failure
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        test_name = request.node.nodeid
        error_message = "Test Failed"

        if hasattr(request.node.rep_call, "longrepr"):
            error_str = str(request.node.rep_call.longrepr)
            if "AssertionError:" in error_str:
                error_message = error_str.split("AssertionError:")[-1].strip().split("\n")[0]
            elif error_str:
                lines = error_str.split("\n")
                for line in lines:
                    if line.strip() and not line.startswith("E ") and len(line.strip()) > 10:
                        error_message = line.strip()
                        break
        screenshot_util.take_failure_screenshot(test_name, error_message)


# --------------------------
# Hook to get test report
# --------------------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


# --------------------------
# Login / Logout fixture
# --------------------------
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
