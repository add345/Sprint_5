#Проверь переход по клику на «Личный кабинет»..

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import conftest


def test_personal_account_click(driver_login):


    driver_login.find_element(By.XPATH, "//a[p[contains(text(), 'Личный Кабинет')]]").click()

    # Добавь явное ожидание для загрузки страницы
    # WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))
    WebDriverWait(driver_login, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))

    # Проверь, что текущий url равен 'https://qa-mesto.praktikum-services.ru/'
    assert driver_login.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    driver_login.quit()