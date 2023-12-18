import os
import time

import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from elements.endpoints import Endpoints
from elements.locators import BasePageLocators
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def accept_cookie(driver):
    driver.get(Endpoints.PORTAL_URL)
    try:
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'acceptCookieButton'))
        )
        cookie_button.click()
    except Exception as e:
        print(f"An error occurred: {e}")


@pytest.fixture()
def api_login():
    # Параметры для входа в API
    api_url = "https://www.airbnb.com/api/v2/login_for_web?key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=PLN&locale=en"
    payload = {
        "metadata": {"sxsMode": "OFF"},
        "fromWeb": True,
        "queryParams": '{"redirect_params":"{}"}',
        "authenticationParams": {
            "email": {"email": "maryjashum@gmail.com", "password": "X9[j5f5H5/"}
        }
    }

    # Отправка запроса на вход
    response = requests.post(api_url, json=payload)

    # Проверка успешности запроса
    if response.status_code == 200:
        # Извлечение токена из ответа
        access_token = response.json().get("access_token")

        # Возвращение токена для использования в тестах
        return access_token
    else:
        # Если запрос неудачен, вызываем исключение, чтобы тест завершился неудачей
        pytest.fail(f"Failed to log in via API. Status code: {response.status_code}, Response: {response.text}")


@pytest.fixture
def logged_in_browser(driver):
    driver.get(Endpoints.PORTAL_URL)
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.CLASS_NAME, "Iiab0gVMeWOd4XcyJGA3 wPxWIS_rJCpwAWksE0s3 Ut3prtt_wDsi7NM_83Jc TuDOVH9WFSdot9jLyXlw EJWUAldA4O1mP0SSFXPm whxYYRnvyHGyGqxO4ici")

    # Вводим логин и пароль
    username_input.send_keys("maryjashum@gmail.com")
    submit_button.click()
    password_input.send_keys("48X013w8fx")

    # Нажимаем кнопку входа
    login_button = driver.find_element(By.CLASS_NAME, "Iiab0gVMeWOd4XcyJGA3 wPxWIS_rJCpwAWksE0s3 Ut3prtt_wDsi7NM_83Jc TuDOVH9WFSdot9jLyXlw EJWUAldA4O1mP0SSFXPm whxYYRnvyHGyGqxO4ici")
    login_button.click()

    # Ждем, пока произойдет переход после успешного входа (предполагается, что есть элемент на следующей странице)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="b2indexPage"]/div[3]/div/header/nav[1]/div[2]/div/span/button/span/div/div[2]/div[1]'))
        )
    except:
        raise Exception("Unable to login")

    yield driver

    # Завершение работы теста - закрытие браузера
    driver.quit()


@pytest.fixture(scope='function', autouse=True)
def make_failed_screenshot(request, driver):
    yield
    if request.session.testsfailed > 0:
        screenshot_file = f"screenshot_{request.node.name}.png"
        driver.get_screenshot_as_file(screenshot_file)
        print(f"Screenshot saved: {screenshot_file}")
