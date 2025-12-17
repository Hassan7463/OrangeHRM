from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def navigate_to(self, base_url):
        self.driver.get(base_url)

    def clear(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()

    def get_all_texts(self, locator):
        elements = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        return [el.text for el in elements]

    def select_by_index(self, locator, index):
        element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        select = Select(element)
        select.select_by_index(index)

    def select_by_visible_text(self, locator, text):
        element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        select = Select(element)
        select.select_by_visible_text(text)

    def select_by_value(self, locator, value):
        element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        select = Select(element)
        select.select_by_value(value)

    def click(self, locator):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        return element.text

    def get_texts(self, locator):
      elements = WebDriverWait(self.driver, self.timeout).until(
        EC.presence_of_all_elements_located(locator))
      return [element.text for element in elements]

    def is_displayed(self, locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
            return element.is_displayed()
        except:
            return False

    def is_enabled(self, locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
            return element.is_enabled()
        except:
            return False

    def is_selected(self, locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
            return element.is_selected()
        except:
            return False
