import allure
from elements.locators import LoginLocators
from pages.login_page import AirbnbLoginTest


# 8
@allure.feature("Login tests")
def test_login(driver):
    login = AirbnbLoginTest(driver)
    login.open_login_page()
    login.close_popup()
    login.perform_login(LoginLocators.EMAIL_INPUT, LoginLocators.PASSWORD_INPUT)
    login.asser_personal_data_presented()
    print(driver.current_url)
