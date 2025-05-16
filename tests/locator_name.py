from selenium.webdriver.common.by import By
# кнопки "начинки"
nach_btn = {'by': By.XPATH, 'value': "//span[contains(text(), 'Начинки')]"}
nach_btn_current = {'by': By.XPATH, 'value': "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[contains(text(), 'Начинки')]"}
# кнопки "булки"
bul_btn = {'by': By.XPATH, 'value': "//span[contains(text(), 'Булки')]"}
bul_btn_current = {'by': By.XPATH, 'value': "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[contains(text(), 'Булки')]"}
# кнопки "соусы"
sauce_btn = {'by': By.XPATH, 'value': "//span[contains(text(), 'Соусы')]"}
sauce_btn_current = {'by': By.XPATH, 'value': "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[contains(text(), 'Соусы')]"}
# поле ввода имени
name_field = {'by': By.XPATH, 'value': "//div[label[contains(text(), 'Имя')]]/input"}
# поле ввода email
email_field = {'by': By.XPATH, 'value': "//div[label[contains(text(), 'Email')]]/input"}
# поле ввода пароля
pswd_field = {'by': By.XPATH, 'value': "//div[label[contains(text(), 'Пароль')]]/input"}
# кнопка "войти"
enter_btn = {'by': By.CSS_SELECTOR, 'value': "form button"}
# кнопка "зарегистрироваться"
register_btn = {'by': By.CLASS_NAME, 'value': "button_button__33qZ0"}
# кнопка "личный кабинет"
person_cab_btn = {'by': By.XPATH, 'value': "//a[p[contains(text(), 'Личный Кабинет')]]"}
# кнопка "войти"
enter_per_cab_btn = {'by': By.XPATH, 'value': "//a[contains(text(), 'Войти')]"}
# кнопка "выход"
exit_btn = {'by': By.XPATH, 'value': "//button[contains(text(), 'Выход')]"}
# уведомление "некорректный пароль"
inpt_err_msg = {'by': By.CLASS_NAME, 'value': 'input__error'}
