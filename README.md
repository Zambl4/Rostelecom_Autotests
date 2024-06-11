# Rostelecom_Autotests

Интерпретатор - Python 3.8

Использован Chrome и драйвер для него Version 125.0.6422.142 (Official Build) (64-bit)
Библиотеки selenium== 4.9.0, pytest-selenium== 4.0.0, pytest== 6.2.5

Тесты разбиты на два файла:
1. test_rostelecom - базовые проверки интерфейса - 10 шт - Запускать командой python -m pytest -v --driver Chrome --driver-path c:\qa\chromedriver\chromedriver-win64\chromedriver.exe test_rostelecom.py
2. test_rostelecom_authorization.py - тесты авторизации - 10 шт - Запускать командой python -m pytest -v --driver Chrome --driver-path c:\qa\chromedriver\chromedriver-win64\chromedriver.exe test_rostelecom_authorization.py

Везде добавлены ожидания по 20 секунд для ввода капчи.
