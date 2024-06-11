# Запускать командой python -m pytest -v --driver Chrome --driver-path c:\qa\chromedriver\chromedriver-win64\chromedriver.exe test_rostelecom.py
# драйвер для хрома Version 125.0.6422.142 (Official Build) (64-bit)
#версии selenium== 4.9.0, pytest-selenium== 4.0.0, pytest== 6.2.5

#Базовые проверки элементов интерфейса страницы

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse

def test_open_page(selenium):
    """ Тест 1. Проверяем открывается ли страница авторизации. """

    selenium.get('https://b2c.passport.rt.ru/account_b2c/page')

    time.sleep(3)

    #проверяем есть ли на открытой странице надпись "Авторизация"
    assert selenium.find_element(By.ID, "card-title").text == 'Авторизация'



def test_open_forgot_password(selenium):
    """ Тест 2. Кнопка "Забыл пароль" ведёт на страницу восстановления пароля. """

    selenium.get('https://b2c.passport.rt.ru/account_b2c/page')

    #ожидание, когда кнопка станет кликабельной
    WebDriverWait(selenium, 20).until(EC.element_to_be_clickable((By.ID, "forgot_password")))

    #находим кнопку и кликаем
    forgot_password_btn = selenium.find_element(By.ID, "forgot_password")
    forgot_password_btn.click()

    time.sleep(3)

    # проверяем есть ли на открытой странице надпись "Восстановление пароля"
    assert selenium.find_element(By.ID, "card-title").text == 'Восстановление пароля'


def test_open_registration(selenium):
    """ Тест 3. Кнопка "Зарегистрироваться" ведёт на страницу регистрации """

    selenium.get('https://b2c.passport.rt.ru/account_b2c/page')

    #ожидание, когда кнопка станет кликабельной
    WebDriverWait(selenium, 20).until(EC.element_to_be_clickable((By.ID, "kc-register")))

    registration_btn = selenium.find_element(By.ID, "kc-register")
    registration_btn.click()

    time.sleep(3)

    # проверяем есть ли на открытой странице надпись "Регистрация"
    assert selenium.find_element(By.ID, "card-title").text == 'Регистрация'



def test_open_agreement(selenium):
    """ Тест 4. Кнопака "пользовательского соглашения" ведёт на страницу соглашения """

    selenium.get('https://b2c.passport.rt.ru/account_b2c/page')

    # ожидание, когда кнопка станет кликабельной
    WebDriverWait(selenium, 20).until(EC.element_to_be_clickable((By.ID, "rt-auth-agreement-link")))

    #находим кнопку соглашения и кликаем
    agreement_btn = selenium.find_element(By.ID, "rt-auth-agreement-link")
    agreement_btn.click()

    time.sleep(3)

    #переключаемся в новое открытое окно
    selenium.switch_to.window(selenium.window_handles[1])

    #проверяем, что в новой вкладке открылся URL пользовательского соглашения

    assert selenium.current_url == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'



def test_open_cookies_tip(selenium):
    """ Тест 5. Кнопка "Cookies" открывает подсказку с информацией о кукис """

    selenium.get('https://b2c.passport.rt.ru/account_b2c/page')

    #ждем загрузку и скроллим страницу вниз
    time.sleep(10)
    selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #ожидание, когда кнопка кукис станет кликабельной
    WebDriverWait(selenium, 20).until(EC.element_to_be_clickable((By.ID, "cookies-tip-open")))

    cookies_btn = selenium.find_element(By.ID, "cookies-tip-open")
    cookies_btn.click()

    time.sleep(3)

    assert selenium.find_element(By.XPATH, '//*[@id="app-footer"]/div[1]/div[2]/span[1]/div[1]/div[2]/span[1]').text == 'Мы используем Cookie'



def test_open_help(selenium):
    """Тест 6. Кнопка "Помощь" открывает страницу помощи"""

    selenium.get('https://b2c.passport.rt.ru/account_b2c/page')

    # ожидание, когда кнопка кукис станет кликабельной
    WebDriverWait(selenium, 20).until(EC.element_to_be_clickable((By.ID, "faq-open")))

    help_btn = selenium.find_element(By.ID, 'faq-open')
    help_btn.click()

    time.sleep(3)

    #проверяем что в заголовке страницы есть текст Ваш безопасный ключ к сервисам Ростелекома
    assert selenium.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/div[1]/div[1]/h1[1]').text == 'Ваш безопасный ключ к сервисам Ростелекома'



def test_open_legal(selenium):
    """ Тест 7. Кнопка "Политикой конфиденциальности" ведёт на страницу c политикой"""

    selenium.get('https://b2c.passport.rt.ru/account_b2c/page')

    # ждем загрузку и скроллим страницу вниз к подвалу
    time.sleep(10)
    element_to_scroll_to = selenium.find_element(By.XPATH, '//*[@id="app-footer"]')
    selenium.execute_script("arguments[0].scrollIntoView();", element_to_scroll_to)
    time.sleep(5)

    #ожидание, когда кнопка политики станет кликабельной
    WebDriverWait(selenium, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app-footer"]/div[1]/div[2]/a[1]/span[1]')))

    # находим кнопку политики и кликаем
    agreement_btn = selenium.find_element(By.XPATH, '//*[@id="app-footer"]/div[1]/div[2]/a[1]/span[1]')
    agreement_btn.click()

    time.sleep(3)

    # переключаемся в новое открытое окно
    selenium.switch_to.window(selenium.window_handles[1])

    time.sleep(3)

    # проверяем, что в путь заказчивается на legal
    assert urlparse(selenium.current_url).path.endswith("legal")



def test_open_vk_authorization(selenium):
    """Тест 8. Проверяем, что кнопка соцсетей "ВК" открывает форму входа"""

    selenium.get('https://b2c.passport.rt.ru/account_b2c/page')

    # ожидание, когда кнопка вк станет кликабельной
    WebDriverWait(selenium, 20).until(EC.element_to_be_clickable((By.ID, "oidc_vk")))

    help_btn = selenium.find_element(By.ID, 'oidc_vk')
    help_btn.click()

    time.sleep(5)

    #проверяем что текущий УРЛ начинается с https://id.vk.com/
    assert selenium.current_url.startswith('https://id.vk.com/')



def test_open_odnoklassniki_authorization(selenium):
    """Тест 9. Проверяем, что кнопка соцсетей "Одноклассники" открывает форму входа"""

    selenium.get('https://b2c.passport.rt.ru/account_b2c/page')

    # ожидание, когда кнопка ОК станет кликабельной
    WebDriverWait(selenium, 20).until(EC.element_to_be_clickable((By.ID, "oidc_ok")))

    help_btn = selenium.find_element(By.ID, 'oidc_ok')
    help_btn.click()

    time.sleep(5)

    #проверяем что текущий УРЛ начинается с https://connect.ok.ru/
    assert selenium.current_url.startswith('https://connect.ok.ru/')



def test_open_mailru_authorization(selenium):
    """Тест 10. Проверяем, что кнопка соцсетей "Мэйл ру" открывает форму входа через мэйлру"""

    selenium.get('https://b2c.passport.rt.ru/account_b2c/page')

    # ожидание, когда кнопка ОК станет кликабельной
    WebDriverWait(selenium, 20).until(EC.element_to_be_clickable((By.ID, "oidc_mail")))

    help_btn = selenium.find_element(By.ID, 'oidc_mail')
    help_btn.click()

    time.sleep(5)

    #проверяем что текущий УРЛ начинается с https://connect.mail.ru/oauth/
    assert selenium.current_url.startswith('https://connect.mail.ru/oauth/')



