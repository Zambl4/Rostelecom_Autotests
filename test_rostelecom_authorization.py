#Запускать командой python -m pytest -v --driver chrome --driver-path c:\qa\chromedriver\chromedriver-win64\chromedriver.exe test_rostelecom_authorization.py
#драйвер для хрома Version 125.0.6422.142 (Official Build) (64-bit)
#версии selenium== 4.9.0, pytest-selenium== 4.0.0, pytest== 6.2.5

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_phone_auth_empty_fields(selenium):
    """ Тест 1. Базовый негативный тест. Пустые поля"""

    selenium.get('https://b2c.passport.rt.ru/account_b2c/page')

    #ожидание, пока поле телефон станет кликабельно
    WebDriverWait(selenium, 10).until(EC.element_to_be_clickable((By.ID, "username")))

    time.sleep(20)

    #ищем кнопку и жмякаем
    search_button = selenium.find_element(By.ID, "kc-login")
    search_button.submit()

    #проверяем, что появилась надпись Неверный логин или пароль
    assert selenium.find_element(By.XPATH, "//*[@id='form-error-message']").text == 'Неверный логин или пароль'


def test_phone_auth_success(selenium):
    """ Тест 2. Позитивный тест. Вход по телефону. Успешный"""

    selenium.get('https://b2c.passport.rt.ru/account_b2c/page')

    #ожидание, пока поле телефон станет кликабельно
    WebDriverWait(selenium, 10).until(EC.element_to_be_clickable((By.ID, "username")))

    # ищем поле телефон и вводим корректное значение
    field_phone = selenium.find_element(By.ID, "username")
    field_phone.clear()
    field_phone.send_keys("79992332030")

    # ищем поле пароль и вводим корректное значение
    field_pass = selenium.find_element(By.ID, "password")
    field_pass.clear()
    field_pass.send_keys("Kolbasa1234")

    time.sleep(30) #пауза для устранения капч

    #ищем кнопку
    search_button = selenium.find_element(By.ID, "kc-login")
    search_button.submit()

    time.sleep(5)

    #проверяем, что на открытой странице есть фамилия Тестировщицкий
    assert selenium.find_element(By.CLASS_NAME, "user-name__last-name").text == 'Тестировщицкий'


def test_phone_auth_invalid_number(selenium):
    """ Тест 3. Негативный тест. Вход по телефону. Неверный телефон: неполный номер"""

    selenium.get('https://b2c.passport.rt.ru/account_b2c/page')

    #ожидание, пока поле телефон станет кликабельно
    WebDriverWait(selenium, 10).until(EC.element_to_be_clickable((By.ID, "username")))

    # ищем поле телефон и вводим некорректное значение
    field_phone = selenium.find_element(By.ID, "username")
    field_phone.clear()
    field_phone.send_keys("7999233")

    # ищем поле пароль и вводим корректное значение
    field_pass = selenium.find_element(By.ID, "password")
    field_pass.clear()
    field_pass.send_keys("Kolbasa1234")

    time.sleep(5)

    #ищем кнопку
    search_button = selenium.find_element(By.ID, "kc-login")
    search_button.submit()

    time.sleep(5)

    #проверяем, что появились надписи Неверный логин или пароль и Неверный формат телефона
    assert selenium.find_element(By.XPATH, "//*[@id='form-error-message']").text == 'Неверный логин или пароль'


def test_phone_auth_invalid_password_20(selenium):
    """ Тест 4. Негативный тест. Вход по телефону. Неверный пароль: 20 символов, кириллица - граничное значение бизнес-логики"""

    selenium.get('https://b2c.passport.rt.ru/account_b2c/page')

    #ожидание, пока поле телефон станет кликабельно
    WebDriverWait(selenium, 10).until(EC.element_to_be_clickable((By.ID, "username")))

    # ищем поле телефон и вводим корректное значение
    field_phone = selenium.find_element(By.ID, "username")
    field_phone.clear()
    field_phone.send_keys("79992332030")

    # ищем поле пароль и вводим некорректное значение
    field_pass = selenium.find_element(By.ID, "password")
    field_pass.clear()
    field_pass.send_keys("Ark16Ark16Ark16Ark16")

    time.sleep(5)

    #ищем кнопку
    search_button = selenium.find_element(By.ID, "kc-login")
    search_button.submit()

    time.sleep(5)

    #проверяем, что появилась надпись Неверный логин или пароль
    assert selenium.find_element(By.XPATH, "//*[@id='form-error-message']").text == 'Неверный логин или пароль'


def test_email_auth_success(selenium):
    """ Тест 5. Позитивный тест. Вход по почте. Успешный"""

    selenium.get('https://b2c.passport.rt.ru/account_b2c/page')

    #ожидание, пока поле телефон станет кликабельно
    WebDriverWait(selenium, 20).until(EC.element_to_be_clickable((By.ID, "username")))

    #находим элемент вкладки почта и кликаем на него
    search_button = selenium.find_element(By.ID, "t-btn-tab-mail")
    search_button.submit()

    time.sleep(3)

    # ищем поле телефон и вводим корректное значение
    field_phone = selenium.find_element(By.ID, "username")
    field_phone.clear()
    field_phone.send_keys("ilia.zamchalkin@gmail.com")

    # ищем поле пароль и вводим корректное значение
    field_pass = selenium.find_element(By.ID, "password")
    field_pass.clear()
    field_pass.send_keys("Kolbasa1234")

    time.sleep(30)  # пауза для устранения капч

    #ищем кнопку
    search_button = selenium.find_element(By.ID, "kc-login")
    search_button.submit()

    time.sleep(5)

    # проверяем, что на открытой странице есть фамилия Тестировщицкий
    assert selenium.find_element(By.CLASS_NAME, "user-name__last-name").text == 'Тестировщицкий'



def test_phone_auth_empty_field(selenium):
    """ Тест 6. Негативный. Вход по почте. Некорректная почта: пустое поле"""

    selenium.get('https://b2c.passport.rt.ru/account_b2c/page')

    #ожидание, пока поле телефон станет кликабельно
    WebDriverWait(selenium, 10).until(EC.element_to_be_clickable((By.ID, "username")))

    # находим элемент вкладки почта и кликаем на него
    search_button = selenium.find_element(By.ID, "t-btn-tab-mail")
    search_button.submit()

    time.sleep(5) #смотри переключение вкладки

    # ищем поле пароль и вводим некорректное значение
    field_pass = selenium.find_element(By.ID, "password")
    field_pass.clear()
    field_pass.send_keys("azXCFEBDvhpgqrKLOIcwt")

        # ищем кнопку
    search_button = selenium.find_element(By.ID, "kc-login")
    search_button.submit()

    #проверяем, что появилась надпись Неверный логин или пароль
    time.sleep(5)

    # проверяем, что появилась надпись Неверный логин или пароль
    assert selenium.find_element(By.XPATH, "//*[@id='form-error-message']").text == 'Неверный логин или пароль'


#здесь снова всплывает капча
def test_phone_auth_invalid_password_21(selenium):
    """ Тест 7. Негативный. Вход по почте. Некорректный пароль: 21 символ - выход за граничное значение БЛ"""

    selenium.get('https://b2c.passport.rt.ru/account_b2c/page')

    #ожидание, пока поле телефон станет кликабельно
    WebDriverWait(selenium, 10).until(EC.element_to_be_clickable((By.ID, "username")))

    # находим элемент вкладки почта и кликаем на него
    search_button = selenium.find_element(By.ID, "t-btn-tab-mail")
    search_button.submit()

    # ищем поле телефон и вводим корректное значение
    field_phone = selenium.find_element(By.ID, "username")
    field_phone.clear()
    field_phone.send_keys("ilia.zamchalkin@gmail.com")

    # ищем поле пароль и вводим некорректное значение
    field_pass = selenium.find_element(By.ID, "password")
    field_pass.clear()
    field_pass.send_keys("azXCFEBDvhpgqrKLOIcwt")

    time.sleep(30) #на случай капчи

        # ищем кнопку
    search_button = selenium.find_element(By.ID, "kc-login")
    search_button.submit()

    #проверяем, что появилась надпись Неверный логин или пароль
    time.sleep(5)

    # проверяем, что появилась надпись Неверный логин или пароль
    assert selenium.find_element(By.XPATH, "//*[@id='form-error-message']").text == 'Неверный логин или пароль'


def test_login_auth_success(selenium):
    """ Тест 8. Позитивный тест. Вход по логину. Успешный"""

    selenium.get('https://b2c.passport.rt.ru/account_b2c/page')

    #ожидание, пока поле телефон станет кликабельно
    WebDriverWait(selenium, 10).until(EC.element_to_be_clickable((By.ID, "username")))

    #находим элемент вкладки Логин и кликаем на него
    search_button = selenium.find_element(By.ID, "t-btn-tab-login")
    search_button.submit()

    # ищем поле телефон и вводим корректное значение
    field_phone = selenium.find_element(By.ID, "username")
    field_phone.clear()
    field_phone.send_keys("lk_5151062")

    # ищем поле пароль и вводим корректное значение
    field_pass = selenium.find_element(By.ID, "password")
    field_pass.clear()
    field_pass.send_keys("Kolbasa1234")

    time.sleep(30) #пауза для устранения капч

    #ищем кнопку
    search_button = selenium.find_element(By.ID, "kc-login")
    search_button.submit()

    time.sleep(5)

    # проверяем, что на открытой странице есть фамилия Тестировщицкий
    assert selenium.find_element(By.CLASS_NAME, "user-name__last-name").text == 'Тестировщицкий'



def test_login_auth_invalid_password_1l(selenium):
    """ Тест 9. Негативный тест. Вход по логину. Неверный пароль: 1 символ - граничное значение"""

    selenium.get('https://b2c.passport.rt.ru/account_b2c/page')

    #ожидание, пока поле телефон станет кликабельно
    WebDriverWait(selenium, 20).until(EC.element_to_be_clickable((By.ID, "username")))

    #находим элемент вкладки Логин и кликаем на него
    search_button = selenium.find_element(By.ID, "t-btn-tab-login")
    search_button.submit()

    time.sleep(5)

    # ищем поле телефон и вводим корректное значение
    field_phone = selenium.find_element(By.ID, "username")
    field_phone.clear()
    field_phone.send_keys("lk_5151062")

    # ищем поле пароль и вводим некорректное значение
    field_pass = selenium.find_element(By.ID, "password")
    field_pass.clear()
    field_pass.send_keys("A")

    time.sleep(5) #здесь боремся с капчей

    #ищем кнопку
    search_button = selenium.find_element(By.ID, "kc-login")
    search_button.submit()

    time.sleep(5)

    # проверяем, что появилась надпись Неверный логин или пароль
    assert selenium.find_element(By.XPATH, "//*[@id='form-error-message']").text == 'Неверный логин или пароль'


def test_login_auth_invalid_password_none(selenium):
    """ Тест 10. Негативный тест. Вход по логину. Неверный пароль: спецсимволы"""

    selenium.get('https://b2c.passport.rt.ru/account_b2c/page')

    #ожидание, пока поле телефон станет кликабельно
    WebDriverWait(selenium, 10).until(EC.element_to_be_clickable((By.ID, "username")))

    #находим элемент вкладки Логин и кликаем на него
    search_button = selenium.find_element(By.ID, "t-btn-tab-login")
    search_button.submit()

    time.sleep(5)

    # ищем поле телефон и вводим корректное значение
    field_phone = selenium.find_element(By.ID, "username")
    field_phone.clear()
    field_phone.send_keys("lk_5151062")

    # ищем поле пароль и вводим некорректное значение
    field_pass = selenium.find_element(By.ID, "password")
    field_pass.clear()
    field_pass.send_keys("!@#$%^&*()_+-=")

    time.sleep(20)

    #ищем кнопку
    search_button = selenium.find_element(By.ID, "kc-login")
    search_button.submit()

    time.sleep(5)

    # проверяем, что появилась надпись Неверный логин или пароль
    assert selenium.find_element(By.XPATH, "//*[@id='form-error-message']").text == 'Неверный логин или пароль'






