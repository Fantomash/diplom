from elements.locators import FlightsPageLocators


class FlightsPage:
    def select_oneway_flight_type(driver):
        driver.find_element(FlightsPageLocators.ONEWAY_RADIOBUTTON).click()

    def select_multistop_flight_type(driver):
        driver.find_element(FlightsPageLocators.MULTICITY_RADIOBUTTON).click()
