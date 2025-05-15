

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import conftest

def test_entrance(login):

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    # Найди поле "Email" и заполни его
    driver.find_element(By.XPATH, "//div[label[contains(text(), 'Email')]]/input").send_keys(login["login"])

    # Найди поле "Пароль" и заполни его
    driver.find_element(By.XPATH, "//div[label[contains(text(), 'Пароль')]]/input").send_keys(login["password"])

    # Найди кнопку "Войти" и кликни по ней
    driver.find_element(By.CSS_SELECTOR, "form button").click()

    # Добавь явное ожидание для загрузки страницы
    # WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    # Проверь, что текущий url равен 'https://qa-mesto.praktikum-services.ru/'
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()

def test_entrance_personal_account(login):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    # Найди кнопку "Личный кабинет" и кликни по ней
    driver.find_element(By.XPATH, "//a[p[contains(text(), 'Личный Кабинет')]]").click()

    # Найди поле "Email" и заполни его
    driver.find_element(By.XPATH, "//div[label[contains(text(), 'Email')]]/input").send_keys(login["login"])

    # Найди поле "Пароль" и заполни его
    driver.find_element(By.XPATH, "//div[label[contains(text(), 'Пароль')]]/input").send_keys(login["password"])

    # Найди кнопку "Войти" и кликни по ней
    driver.find_element(By.CSS_SELECTOR, "form button").click()

    # Добавь явное ожидание для загрузки страницы
        # WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    # Проверь, что текущий url равен 'https://qa-mesto.praktikum-services.ru/'
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()


def test_entrance_register_form(login):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")


    # Найди кнопку "Войти" и кликни по ней
    driver.find_element(By.XPATH, "//a[contains(text(), 'Войти')]").click()

    # Найди поле "Email" и заполни его
    driver.find_element(By.XPATH, "//div[label[contains(text(), 'Email')]]/input").send_keys(login["login"])

    # Найди поле "Пароль" и заполни его
    driver.find_element(By.XPATH, "//div[label[contains(text(), 'Пароль')]]/input").send_keys(login["password"])

    # Найди кнопку "Войти" и кликни по ней
    driver.find_element(By.CSS_SELECTOR, "form button").click()

    # Добавь явное ожидание для загрузки страницы
    # WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    # Проверь, что текущий url равен 'https://qa-mesto.praktikum-services.ru/'
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()

def test_entrance_password_recovery(login):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")


    # Найди кнопку "Воccтановить пароль" и кликни по ней
    driver.find_element(By.XPATH, "//a[contains(text(), 'Войти')]").click()

    # Найди поле "Email" и заполни его
    driver.find_element(By.XPATH, "//div[label[contains(text(), 'Email')]]/input").send_keys(login["login"])

    # Найди поле "Пароль" и заполни его
    driver.find_element(By.XPATH, "//div[label[contains(text(), 'Пароль')]]/input").send_keys(login["password"])

    # Найди кнопку "Войти" и кликни по ней
    driver.find_element(By.CSS_SELECTOR, "form button").click()

    # Добавь явное ожидание для загрузки страницы
    # WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    # Проверь, что текущий url равен 'https://qa-mesto.praktikum-services.ru/'
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()