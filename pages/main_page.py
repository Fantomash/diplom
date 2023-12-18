import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from elements.endpoints import Endpoints
from elements.locators import BasePageLocators
from pages import BasePage


class MainPage(BasePage):
    MAIN_LOGO = ('//*[@id="react-application"]/div/div/div[1]/div/div[3]/div[1]/div/div/div/header/div/div[1]/a')

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Browser starts")
    def open_main_page(self):
        self.driver.get(Endpoints.PORTAL_URL)

    @allure.step("Browser starts")
    def open_main_page_and_close_popup(self):
        self.driver.get(Endpoints.PORTAL_URL)
        wait = WebDriverWait(self.driver, 10)
        cross_button = wait.until(EC.visibility_of_element_located((By.XPATH, BasePageLocators.CROSS_POPUP_BUTTON)))
        if cross_button.is_displayed():
            cross_button.click()

    def assert_main_logo_presented(self):
        assert self.driver.assert_element_is_presented(self.MAIN_LOGO), "Logo is not presented"

    @allure.step("Introducing Guest Favorites popup is closing")
    def close_popup(self):
        wait = WebDriverWait(self.driver, 10)
        cross_button = wait.until(EC.visibility_of_element_located((By.XPATH, BasePageLocators.CROSS_POPUP_BUTTON)))
        if cross_button.is_displayed():
            cross_button.click()

    @allure.step("Searching for text")
    def find_text(self, by, locator):
        wait = WebDriverWait(self.driver, 10)
        support_title = wait.until(EC.visibility_of_element_located((by, locator)))
        return support_title

    @allure.step("Searching for elements")
    def get_elements(self, by, locator):
        elements = self.driver.find_elements(by, locator)
        return elements

    @allure.step("Searching for element")
    def get_element(self, by, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((by, locator)))
        return element

    @allure.step("Click on element")
    def click_element(self, by, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((by, locator)))
        element.click()

    @allure.step("Menu profile is opening")
    def open_profile_menu(self):
        wait = WebDriverWait(self.driver, 10)
        profile_menu = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, BasePageLocators.MAIN_NAVIGATION_MENU)))
        profile_menu.click()

    @allure.step("Click on a menu item")
    def click_menu_item(self, locator):
        wait = WebDriverWait(self.driver, 10)
        menu_item = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        menu_item.click()

    @allure.step("Open filter menu")
    def open_filter_menu(self):
        wait = WebDriverWait(self.driver, 10)
        filter_menu = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, BasePageLocators.FILTER)))
        filter_menu.click()