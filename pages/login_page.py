import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import credentials

from elements.endpoints import Endpoints
from elements.locators import BasePageLocators, LoginLocators


class AirbnbLoginTest:
    def __init__(self, driver, WAIT_UNTIL=10):
        self.driver = driver
        self.WAIT_UNTIL = WAIT_UNTIL

    def open_login_page(self):
        self.driver.get(Endpoints.PORTAL_URL)

    def switch_to_modal_window(self):
        main_window_handle = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != main_window_handle:
                self.driver.switch_to.window(handle)
                break

    def perform_login(self, username, password):
        wait = WebDriverWait(self.driver, 10)
        profile_menu = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, BasePageLocators.MAIN_NAVIGATION_MENU)))
        profile_menu.click()
        login = wait.until(EC.visibility_of_element_located((By.XPATH, BasePageLocators.LOGIN_MENU_ITEM)))
        login.click()
        google_button = wait.until(EC.visibility_of_element_located((By.XPATH, LoginLocators.LOGIN_WITH_GOOGLE)))
        google_button.click()
        self.switch_to_modal_window()
        with allure.step("Enter an email"):
            email_input = wait.until(EC.visibility_of_element_located((By.ID, username)))
            email_input.send_keys(credentials.AIRBNB_LOGIN)
            next_button_login = wait.until(EC.visibility_of_element_located((By.ID, LoginLocators.NEXT_BUTTON_LOGIN)))
            next_button_login.click()
        with allure.step("Enter a password"):
            password_input = wait.until(EC.visibility_of_element_located((By.XPATH, password)))
            password_input.send_keys(credentials.AIRBNB_PASSWORD)
            next_button_password = wait.until(
                EC.visibility_of_element_located((By.XPATH, LoginLocators.NEXT_BUTTON_PASSWORD)))
            next_button_password.click()

    def switch_to_main_window(self):
        handles = self.driver.window_handles
        if len(handles) > 1:
            self.driver.switch_to.window(handles[0])

    def open_account_page(self):
        self.driver.get(Endpoints.ACCOUNT_SETTINGS)

    def asser_personal_data_presented(self):
        personal_data_line = WebDriverWait(self.driver, self.WAIT_UNTIL).until(
            EC.visibility_of_element_located((By.CLASS_NAME, LoginLocators.PERSONAL_DATA)))
        actual_text = personal_data_line.get_attribute('textContent')
        expected_text = credentials.AIRBNB_LOGIN
        assert expected_text in actual_text, f"Expected text is '{expected_text}', but actual text is '{actual_text}'"

    @allure.step("Introducing Guest Favorites popup is closing")
    def close_popup(self):
        wait = WebDriverWait(self.driver, 10)
        cross_button = wait.until(EC.visibility_of_element_located((By.XPATH, BasePageLocators.CROSS_POPUP_BUTTON)))
        if cross_button.is_displayed():
            cross_button.click()

    def close_browser(self):
        self.driver.quit()
