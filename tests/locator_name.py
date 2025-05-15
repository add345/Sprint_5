(By.XPATH, "//div[label[contains(text(), 'Имя')]]/input").send_keys(login['name'] # Поле "Имя"/регистрация
(By.XPATH, "//div[label[contains(text(), 'Email')]]/input").send_keys(login['login']) # Поле "Email/регистрация
(By.CSS_SELECTOR, "input[type=password]").send_keys('111') # Поле "Пароль"/регистрация
(By.CLASS_NAME, "button_button__33qZ0") # Кнопка "Войти"
(By.XPATH, "//a[p[contains(text(), 'Личный Кабинет')]]") # Кнопка "Личный Кабинет"
(By.XPATH, "//button[contains(text(), 'Выход')")  # Кнопка "Выход"/Личный кабинет
(By.XPATH, "//span[contains(text(), 'Начинки')]") # Кнопка "Начинки"


(By.CSS_SELECTOR, "form button")# Кнопка "Войти" на странице https://stellarburgers.nomoreparties.site/login
(By.XPATH, "//a[contains(text(), 'Войти')]") # Кнопка "Восстановить пароль" на странице https://stellarburgers.nomoreparties.site/forgot-password
(By.XPATH, "//div[label[contains(text(), 'Пароль')]]/input")# поле "Пароль"