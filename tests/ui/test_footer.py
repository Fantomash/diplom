import time

import allure
from selenium.webdriver.common.by import By
from elements.locators import BasePageLocators
from pages.main_page import MainPage


# 6
@allure.feature("Footer tests")
def test_support_section(driver):
    footer = MainPage(driver)
    footer.open_main_page()
    footer.close_popup()
    support_title = footer.get_element(By.XPATH, BasePageLocators.SUPPORT_TITLE)
    actual_text = support_title.text
    expected_text = 'Support'
    assert actual_text == expected_text, f"Texts are different. Expected: '{expected_text}', Actual: '{actual_text}'"


# 7
@allure.feature("Footer tests")
def test_inspiration_tabs(driver):
    expected_button_names = ['Popular', 'Arts & culture', 'Outdoors', 'Mountains', 'Beach', 'Unique stays',
                             'Categories',
                             'Things to do', 'Airbnb-friendly apartments']
    tabs = MainPage(driver)
    tabs.open_main_page()
    tabs.close_popup()
    buttons = tabs.get_elements(By.XPATH, BasePageLocators.TABLIST)
    assert len(buttons) == len(expected_button_names)