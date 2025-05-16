#Проверь:
#Успешную регистрацию. Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен: например, 123@ya.ru. Минимальный пароль — шесть символов.
#Ошибку для некорректного пароля.
import locator_name
from data import login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import conftest

@pytest.mark.usefixtures("driver")
class Test_registration:

    def test_registration_negative(self):

        self.driver.get("https://stellarburgers.nomoreparties.site/register")

        self.driver.find_element(**locator_name.name_field).send_keys(login['name'])
        # Найди поле "Email" и заполни его
        self.driver.find_element(**locator_name.email_field).send_keys(login['login'])

        # Найди поле "Пароль" и заполни его
        self.driver.find_element(**locator_name.pswd_field).send_keys('111')

        # Найди кнопку "Войти" и кликни по ней
        self.driver.find_element(**locator_name.register_btn).click()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'input__error')))

        err = self.driver.find_element(**locator_name.inpt_err_msg)

        assert err.is_displayed()

    def test_registration(self):

        self.driver.get("https://stellarburgers.nomoreparties.site/register")

        self.driver.find_element(**locator_name.name_field).send_keys(login['name'])
        # Найди поле "Email" и заполни его
        self.driver.find_element(**locator_name.email_field).send_keys(login['login'])

        # Найди поле "Пароль" и заполни его
        self.driver.find_element(**locator_name.pswd_field).send_keys('111')

        # Найди кнопку "Войти" и кликни по ней
        self.driver.find_element(**locator_name.register_btn).click()

        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        assert self.driver.current_url ==  'https://stellarburgers.nomoreparties.site/login'
