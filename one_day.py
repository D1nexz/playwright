#ФИО: Соколов Антон Сергеевич
#Дата: 2026-11-10
#Время: 12:38
#Описание: Код открывает сайт playwright.dev в браузере Chrome, выводит название в консоль и закрывает браузер
#Я скопировал пример из раздела "начало работы - библиотека" и запустил его

from playwright.sync_api import sync_playwright#берём(импортируем) нужный модуль 

with sync_playwright() as p:#подготовка к работе, запускает playwright
    browser = p.chromium.launch() #запуск браузера
    page = browser.new_page() #открваем страницу браузера
    page.goto("https://playwright.dev")#переходит на сайт playwright
    print(page.title())#выводим заголовок title
    browser.close() #закрываем браузер