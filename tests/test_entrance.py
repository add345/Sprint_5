
import locator_name
from data import login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import conftest

@pytest.mark.usefixtures("driver")
class Test_entrance:

    def test_entrance(self):

        self.driver.get("https://stellarburgers.nomoreparties.site/login")

        # Найди поле "Email" и заполни его
        self.driver.find_element(**locator_name.email_field).send_keys(login["login"])

        # Найди поле "Пароль" и заполни его
        self.driver.find_element(**locator_name.pswd_field).send_keys(login["password"])

        # Найди кнопку "Войти" и кликни по ней
        self.driver.find_element(**locator_name.enter_btn).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

        # Проверь, что текущий url равен 'https://qa-mesto.praktikum-services.ru/'
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_entrance_personal_account(self, driver):
        self.driver.get("https://stellarburgers.nomoreparties.site")

        # Найди кнопку "Личный кабинет" и кликни по ней
        self.driver.find_element(**locator_name.person_cab_btn).click()

        # Найди поле "Email" и заполни его
        self.driver.find_element(**locator_name.email_field).send_keys(login["login"])

        # Найди поле "Пароль" и заполни его
        self.driver.find_element(**locator_name.pswd_field).send_keys(login["password"])

        # Найди кнопку "Войти" и кликни по ней
        self.driver.find_element(**locator_name.enter_btn).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

        # Проверь, что текущий url равен 'https://qa-mesto.praktikum-services.ru/'
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    def test_entrance_register_form(self, driver):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")


        # Найди кнопку "Войти" и кликни по ней
        self.driver.find_element(**locator_name.enter_per_cab_btn).click()

        # Найди поле "Email" и заполни его
        self.driver.find_element(**locator_name.email_field).send_keys(login["login"])

        # Найди поле "Пароль" и заполни его
        self.driver.find_element(**locator_name.pswd_field).send_keys(login["password"])

        # Найди кнопку "Войти" и кликни по ней
        self.driver.find_element(**locator_name.enter_btn).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

        # Проверь, что текущий url равен 'https://qa-mesto.praktikum-services.ru/'
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    def test_entrance_password_recovery(self, driver):
        self.driver.get("https://stellarburgers.nomoreparties.site/forgot-password")


        # Найди кнопку "Воccтановить пароль" и кликни по ней
        self.driver.find_element(**locator_name.enter_per_cab_btn).click()

        # Найди поле "Email" и заполни его
        self.driver.find_element(**locator_name.email_field).send_keys(login["login"])

        # Найди поле "Пароль" и заполни его
        self.driver.find_element(**locator_name.pswd_field).send_keys(login["password"])

        # Найди кнопку "Войти" и кликни по ней
        self.driver.find_element(**locator_name.enter_btn).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

        # Проверь, что текущий url равен 'https://qa-mesto.praktikum-services.ru/'
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/'
