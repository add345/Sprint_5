#Проверь:
#Успешную регистрацию. Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен: например, 123@ya.ru. Минимальный пароль — шесть символов.
#Ошибку для некорректного пароля.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import conftest


def test_registration_negative(login):

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")


    driver.find_element(By.XPATH, "//div[label[contains(text(), 'Имя')]]/input").send_keys(login['name'])
    # Найди поле "Email" и заполни его
    driver.find_element(By.XPATH, "//div[label[contains(text(), 'Email')]]/input").send_keys(login['login'])

    # Найди поле "Пароль" и заполни его
    driver.find_element(By.CSS_SELECTOR, "input[type=password]").send_keys('111')

    # Найди кнопку "Войти" и кликни по ней
    driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'input__error')))

    err = False
    try:
      err = driver.find_element(By.CLASS_NAME, 'input__error')
    except Exception as e:
        err = False
    assert err != False

def test_registration(login):

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(By.XPATH, "//div[label[contains(text(), 'Имя')]]/input").send_keys(login['name'])
    # Найди поле "Email" и заполни его
    driver.find_element(By.XPATH, "//div[label[contains(text(), 'Email')]]/input").send_keys(login['login'])

    # Найди поле "Пароль" и заполни его
    driver.find_element(By.CSS_SELECTOR, "input[type=password]").send_keys(login['password'])

    # Найди кнопку "Войти" и кликни по ней
    driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))
    assert driver.current_url ==  'https://stellarburgers.nomoreparties.site/login'
