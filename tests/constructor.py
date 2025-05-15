#Переход из личного кабинета в конструктор
#Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import conftest


def test_constructor_click(driver_login):

  # Найди кнопку "Конструктор" и кликни по ней
    driver_login.find_element(By.XPATH, "//a[p[contains(text(), 'Конструктор')]]").click()

    # Добавь явное ожидание для загрузки страницы
    # WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))
    WebDriverWait(driver_login, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    # Проверь, что текущий url равен 'https://qa-mesto.praktikum-services.ru/'
    assert driver_login.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver_login.quit()

def test_stellar_burgers_click(driver_login):

  # Найди кнопку "логотип Stellar Burgers" и кликни по ней
    driver_login.find_element(By.XPATH, "//header/nav/div/a[@href='/']").click()

    # Добавь явное ожидание для загрузки страницы
    # WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))
    WebDriverWait(driver_login, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    # Проверь, что текущий url равен 'https://qa-mesto.praktikum-services.ru/'
    assert driver_login.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver_login.quit()