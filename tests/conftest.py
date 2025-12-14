from selenium import webdriver
import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
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