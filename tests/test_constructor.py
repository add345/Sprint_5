#Переход из личного кабинета в конструктор
#Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import conftest

@pytest.mark.usefixtures("driver_login")
class Test_constructor:

  def test_constructor_click(self):

    # Найди кнопку "Конструктор" и кликни по ней
      self.driver.find_element(By.XPATH, "//a[p[contains(text(), 'Конструктор')]]").click()

      # Добавь явное ожидание для загрузки страницы
      # Webself.driverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))
      WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

      # Проверь, что текущий url равен 'https://qa-mesto.praktikum-services.ru/'
      assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/'

  def test_stellar_burgers_click(self):

    # Найди кнопку "логотип Stellar Burgers" и кликни по ней
      self.driver.find_element(By.XPATH, "//header/nav/div/a[@href='/']").click()

      # Добавь явное ожидание для загрузки страницы
      # WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))
      WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

      # Проверь, что текущий url равен 'https://qa-mesto.praktikum-services.ru/'
      assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/'