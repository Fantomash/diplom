import allure
from selenium.webdriver.common.by import By
from elements.endpoints import Endpoints
from elements.locators import BasePageLocators
from pages.main_page import MainPage


# 1
@allure.title("Check availability of a main logo")
@allure.feature("Header tests")
def test_main_logo_displayed(driver):
    main_page = MainPage(driver)
    main_page.open_main_page_and_close_popup()
    main_logo = main_page.get_element(By.CLASS_NAME, BasePageLocators.MAIN_LOGO)
    assert main_logo.is_displayed()


# 2
@allure.feature("Header tests")
@allure.title("Check availability of property icons")
def test_property_icons_displayed(driver):
    main_page = MainPage(driver)
    main_page.open_main_page_and_close_popup()
    rooms_icon = main_page.get_element(By.XPATH, BasePageLocators.ROOMS_ICON)
    views_icon = main_page.get_element(By.XPATH, BasePageLocators.VIEWS_ICON)
    cabins_icon = main_page.get_element(By.XPATH, BasePageLocators.CABIN_ICON)
    assert rooms_icon.is_displayed()
    assert views_icon.is_displayed()
    assert cabins_icon.is_displayed()


# 3
@allure.feature("Header tests")
@allure.title("Check the filter icon is clickable")
def test_filter_is_opening(driver):
    main_page = MainPage(driver)
    main_page.open_main_page_and_close_popup()
    main_page.open_filter_menu()
    filter_menu = main_page.find_text(By.CLASS_NAME, BasePageLocators.FILTER_HEADER)
    actual_header = filter_menu.text
    expected_header = 'Filters'
    assert actual_header == expected_header, f"Texts are different. Expected: '{expected_header}', Actual: '{actual_header}'"


# 4
@allure.feature("Header tests")
@allure.title("Check availability of changing the language")
def test_change_language(driver):
    main_page = MainPage(driver)
    main_page.open_main_page_and_close_popup()
    with allure.step("Click on a language icon"):
        main_page.click_element(By.XPATH, BasePageLocators.LANG_ICON)
    with allure.step("Change a language"):
        main_page.click_element(By.XPATH, BasePageLocators.NEW_LANG)
    current_url = driver.current_url
    assert current_url.startswith(
        Endpoints.EXPECTED_PORTAL_URL), f"Expected URL to start with '{Endpoints.EXPECTED_PORTAL_URL}', but got '{current_url}'"


# 5
@allure.feature("Header tests")
@allure.title("Check availability of Gift cards page")
def test_gift_cards_access(driver):
    giftcard = MainPage(driver)
    giftcard.open_main_page()
    giftcard.close_popup()
    giftcard.open_profile_menu()
    giftcard.click_menu_item(BasePageLocators.GIFT_CARD_MENU_ITEM)
    current_url = driver.current_url
    assert current_url.startswith(
        Endpoints.GIFT_CARDS_URL), f"Expected URL to start with '{Endpoints.GIFT_CARDS_URL}', but got '{current_url}'"
