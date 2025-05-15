import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture # фикстура, которая
def login():
    login = {'name': 'viva1', 'login': 'ekatherina_alexandrova_31@yandex.ru', 'password': '123456'}

    return login


@pytest.fixture # фикстура, которая
def driver_login(login):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    # Найди поле "Email" и заполни его
    driver.find_element(By.XPATH, "//div[label[contains(text(), 'Email')]]/input").send_keys(login["login"])

    # Найди поле "Пароль" и заполни его
    driver.find_element(By.XPATH, "//div[label[contains(text(), 'Пароль')]]/input").send_keys(login["password"])

    # Найди кнопку "Войти" и кликни по ней
    driver.find_element(By.CSS_SELECTOR, "form button").click()

    return driver