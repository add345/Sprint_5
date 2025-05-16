from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import conftest
import locator_name

@pytest.mark.usefixtures("driver")
class Test_construction:

    def test_nach(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(**locator_name.nach_btn).click()
        elm = self.driver.find_element(**locator_name.nach_btn_current)
        assert elm.is_displayed() == True


    def test_bul(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(**locator_name.bul_btn).click()
        elm = self.driver.find_element(**locator_name.nach_btn_current)
        assert elm.is_displayed() == True

    def test_sauce(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(**locator_name.sauce_btn).click()
        elm = self.driver.find_element(**locator_name.sauce_btn_current)
        assert elm.is_displayed() == True
