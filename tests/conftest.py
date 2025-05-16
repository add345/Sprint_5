from urllib3 import request

from data import login
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope="function")
def driver_login(request):
    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.nomoreparties.site/login")

    # Найди поле "Email" и заполни его
    driver.find_element(By.XPATH, "//div[label[contains(text(), 'Email')]]/input").send_keys(login["login"])

    # Найди поле "Пароль" и заполни его
    driver.find_element(By.XPATH, "//div[label[contains(text(), 'Пароль')]]/input").send_keys(login["password"])

    # Найди кнопку "Войти" и кликни по ней
    driver.find_element(By.CSS_SELECTOR, "form button").click()

    request.cls.driver = driver

    yield

    driver.quit()