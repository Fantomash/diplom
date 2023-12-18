from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.helpers import Helpers


class Assertion(Helpers):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assert_text_in_element(self, locator, expected_result):
        element = self.wait_for_visible(locator)
        assert element.text == expected_result, "Text is not the same"

    def assert_value_in_element_attribute(self, locator, attribute, expected_result):
        element = self.wait_for_visible(locator)
        value = element.get_attribute(attribute)
        assert value == expected_result, "Attribute value is not the same"

    def assert_actual_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"

    def assert_element_is_displayed(driver, by, value, timeout=10):
        try:
            Helpers.wait_for_element_is_visible(driver, by, value, timeout)
            return True
        except NoSuchElementException as e:
            print(f"An error occurred: {e}")
            return False
