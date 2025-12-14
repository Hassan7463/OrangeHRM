from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def send_keys(self, locator, text):
        (WebDriverWait(self.driver, 10).
         until(EC.visibility_of_element_located(locator))
         .send_keys(text))

    def get_text(self, locator):
       element =  (WebDriverWait(self.driver, 10).
         until(EC.visibility_of_element_located(locator)))
       return element.text

    def is_displayed(self, locator):
        try:
            element = (WebDriverWait(self.driver, 10).
                   until(EC.visibility_of_element_located(locator)))
            return element.is_displayed()
        except:
            return False


    def is_enabled(self, locator):
        try:
            element = (WebDriverWait(self.driver, 10).
                       until(EC.visibility_of_element_located(locator)))
            return element.is_enabled()
        except:
            return False


    def is_selected(self, locator):
        try:
            element = (WebDriverWait(self.driver, 10).
                       until(EC.visibility_of_element_located(locator)))
            return element.is_selected()
        except:
            return False