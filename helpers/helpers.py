import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, TimeoutException


class Helpers:
    def __init__(self, driver, WAIT_UNTIL=10):
        self.driver = driver
        self.WAIT_UNTIL = WAIT_UNTIL

    @staticmethod
    def wait_for_visible(driver, by, value, timeout=5):
        # by, value = locator
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            return False, f"Element with {by}: {value} is not visible within {timeout} seconds."

    def click_on(self, locator):
        element = self.wait_for_visible(locator)
        element.click()

    def hard_click(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].click();", element)

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_element_is_visible(self, locator, timeout=30):
        element = self.driver.find_element(By.XPATH, locator)
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of(element)
        )

    def find_element(driver, by, value):
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((by, value))
        )

    def wait_for_page_url_change(self, current_url, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            EC.url_changes(current_url)
        )

    def wait_for_page_reload(self, current_url, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            EC.staleness_of(self.driver.find_element(By.TAG_NAME, 'html'))
        )
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.driver.current_url != current_url
        )

    def switch_to_modal_window(self):
        main_window_handle = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != main_window_handle:
                self.driver.switch_to.window(handle)
                break