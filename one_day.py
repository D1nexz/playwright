#ФИО: Соколов Антон Сергеевич
#Дата: 2026-11-10
#Время: 12:38
#Описание: Код открывает сайт playwright.dev в браузере Chrome, выводит название в консоль и закрывает браузер
#Я скопировал пример из раздела "начало работы - библиотека" и запустил его

#установка

#pip install --upgrade pip
#pip install playwright
#playwright install

from playwright.sync_api import sync_playwright#берём(импортируем) нужный модуль 

with sync_playwright() as p:#подготовка к работе, запускает playwright
    browser = p.chromium.launch() #запуск браузера
    page = browser.new_page() #открваем страницу браузера
    page.goto("https://blindtyping.com/ru")#переходит на сайт blindtyping
    print(f"Заголовок: {page.title()}") # Вывод заголовка
    browser.close() #закрываем браузер
# Что модифицировал: я добавил f строку что бы переменные можно было вставлять прямо в текст, так же изменил переход на сайт
# результат запуска: "Заголовок: Тест печати онлайн – развивай скорость и точность с Blind Typing"
# код выполнен без ошибок.