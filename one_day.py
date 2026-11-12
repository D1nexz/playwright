#ФИО: Соколов Антон Сергеевич
#Дата: 2026-11-10
#Время: 12:38
#Описание: Код открывает сайт playwright.dev в браузере Chrome, выводит название в консоль и закрывает браузер
#Я скопировал пример из раздела "начало работы - библиотека" и запустил его

"""Устанорвка"""

#uv self update
#uv add playwright
#playwright install

#from playwright.sync_api import sync_playwright#берём(импортируем) нужный модуль 

#with sync_playwright() as p: # подготовка к работе, запускает playwright
    #browser = p.chromium.launch() # запуск браузера
    #page = browser.new_page() # открваем страницу браузера
    #page.goto("https://blindtyping.com/ru") # переходит на сайт blindtyping
    #print(f"Заголовок: {page.title()}") # Вывод заголовка
    #browser.close() # закрываем браузер
# результат старого запуска: "Playwright"
# Что модифицировал: я добавил f строку что бы переменные можно было вставлять прямо в текст, так же изменил переход на сайт
# результат нового запуска: "Заголовок: Тест печати онлайн – развивай скорость и точность с Blind Typing"
# код выполнен без ошибок.

#ФИО: Соколов Антон Сергеевич
#Дата: 2026-11-10
#Время: 23:52
#Описание: Код открывает сайт playwright.dev в браузере Chrome, выводит название в консоль и закрывает браузер
#Я скопировал пример из раздела "начало работы - библиотека" и запустил его

"""Для современного проекта используется асинхронный API"""

#import asyncio # импорт для запуска
#from playwright.async_api import async_playwright # подключаем асинхронную версию

#async def main(): # создаем функцию и говорим Python что это на подумать, загрузить, просмореть(выполнять асинхронно)
    #async with async_playwright() as p: # запуск Playwright
        #browser = await p.chromium.launch() # запуск праузера 
        #page = await browser.new_page() # открытие новой вкладки
        #await page.goto("https://playwright.dev") # переход на сайт
        #print(await page.title()) # заголовок страницы
        #await browser.close() # закрываем браузер

#asyncio.run(main())
# результат запуска: "Fast and reliable end-to-end testing for modern web apps | Playwright"
# код выполнен без ошибок

#ФИО: Соколов Антон Сергеевич
#Дата: 2026-11-11
#Время: 00:09
#Описание: Код открывает нужную ссылку, запускает браузер(по желанию можно указать любой), делает скрин и закрывает браузер
#Я скопировал пример из раздела "начало работы - библиотека(Первый скрипт)" и запустил его

"""Первый скрипт"""

#from playwright.sync_api import sync_playwright # библиотека для управление браузером

#with sync_playwright() as p: # Запуск Playwright.
    #browser = p.chromium.launch() # запуск браузера chrome
    #page = browser.new_page() # В браузере открывается новая пустая вкладка
    #page.goto("https://monkeytype.com/") # переходит по указанной ссылке
    #page.screenshot(path="example.png") # делает снимок и сохроняет в папку
    #browser.close() # закрывает браузер 

# результат старого запуска: после запуска программы открывается браузер и идёт переход по указанной ссылке, делает скрин, сохроняет скрин в папку и закрывает браюзер
# что модифицировал: изначально запускался браузер Safari(p.webkit) я поменял на баузер Chrome(p.chromium), изменил ссылку по которой переходит код
# результат нового запуска: теперь после запуска открывается браузер не Safari, а Chrome и так же переходит на новый сайт и делает скрин
# код выполнен без ошибок

"""Интерактивный режим"""


#ФИО: Соколов Антон Сергеевич
#Дата: 2026-11-11
#Время: 12:36
#Описание: Код открывает нужную ссылку, запускает браузер(по желанию можно указать любой), делает скрин и закрывает браузер
#Я скопировал пример из раздела "начало работы - библиотека(Интерактивный режим)" и запустил его

#запускаем интерактивную REPL-среду Python в терминале
   #python

#from playwright.sync_api import sync_playwright # Импорт sync_playwright
#playwright = sync_playwright().start() # Запускает Playwright
# Use playwright.chromium, playwright.firefox or playwright.webkit
# Pass headless=False to launch() to see the browser UI
#browser = playwright.chromium.launch() # Запускает Chrome
#page = browser.new_page() # Открывает страницу в браузере
#page.goto("https://www.freecodecamp.org/learn") # Переходит на указанный адрес
#page.screenshot(path="example4.png") # Делает скриншот страницы и сохраняет в файл
#browser.close() # Закрывает браузер
#playwright.stop() # Останавливает Playwright

# я поработал в интерактивном REPl Python
# скрин работы example4.png 
# код выполнен без ошибок

"""Pyinstaller"""

#С помощью Playwright и Pyinstaller можно создавать автономные исполняемые файлы.

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    page.screenshot(path="example5.png")
    browser.close()


