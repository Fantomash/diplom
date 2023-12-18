from selenium.common import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from elements.locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.WAIT_UNTIL = 10
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def enter_destination(self, driver, destination):
        self.driver.find_element(BasePageLocators.DESTINATION_INPUT).send_keys(destination)

    def click_search_button(self, driver):
        self.driver.find_element(BasePageLocators.SEARCH_BUTTON).click()

    def wait_for_visible(self, locator):
        try:
            return WebDriverWait(self.driver, self.WAIT_UNTIL).until(
                EC.visibility_of_element_located((By.XPATH, locator)))
        except WebDriverException:
            assert False, f"Element {locator} is not clickable"

    def assert_element_is_presented(self, locator):
        try:
            self.wait_for_visible(locator)
        except Exception:
            assert False, f"Element {locator} is not presented on the page"

