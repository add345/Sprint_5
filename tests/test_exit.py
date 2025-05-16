import locator_name
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import conftest

@pytest.mark.usefixtures("driver_login")
class Test_exit:

    def test_exit(self):
        # Найди кнопку "Войти" и кликни по ней
        self.driver.find_element(**locator_name.person_cab_btn).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Выход')]")))
        # Найди кнопку "Выход" и кликни по ней
        self.driver.find_element(**locator_name.exit_btn).click()
        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        # Проверь, что текущий url равен 'https://qa-mesto.praktikum-services.ru/'
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
