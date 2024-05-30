import random

from pywinauto.keyboard import send_keys
from pywinauto import Application
import time
from datetime import datetime

def open_telegram():
    # Запуск Telegram (замініть шлях до вашого додатку Telegram, якщо потрібно)
    app = Application().start("C:\\tg\\Telegram Desktop\\Telegram.exe")
    time.sleep(5)  # Зачекаємо, поки додаток відкриється
    return app

def search_botfather(app):
    # Отримання головного вікна Telegram
    main_window = app.window(title_re="Telegram")

    # Використовуємо клавіші для активації поля пошуку
    main_window.type_keys("^f")  # Ctrl + F для активації пошуку
    time.sleep(1)

    # Вводимо 'BotFather' в поле пошуку
    send_keys('BotFather')
    time.sleep(2)  # Зачекаємо, поки результати з'являться

    # Натискаємо Enter для вибору першого результату пошуку
    send_keys('{ENTER}')
    print("Чат з BotFather відкритий.")
    time.sleep(2)

    send_keys('/start')
    time.sleep(0.5)

    send_keys('{ENTER}')
    time.sleep(0.5)

    send_keys('/newbot')
    time.sleep(0.5)

    send_keys('{ENTER}')
    time.sleep(0.5)
    a=range(1,100000000)
    send_keys(f'TeleBot{random.choice(a)}BySpace_bot')
    time.sleep(0.5)
    send_keys('{ENTER}')


if __name__ == "__main__":
    app = open_telegram()
    search_botfather(app)