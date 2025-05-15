from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import conftest


def test_nach():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "//span[contains(text(), 'Начинки')]").click()
    elm = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[contains(text(), 'Начинки')]")
    assert elm.is_displayed() == True


def test_bul():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "//span[contains(text(), 'Начинки')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(), 'Булки')]").click()
    elm = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[contains(text(), 'Булки')]")
    assert elm.is_displayed() == True

def test_sauce():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "//span[contains(text(), 'Соусы')]").click()
    elm = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[contains(text(), 'Соусы')]")
    assert elm.is_displayed() == True
