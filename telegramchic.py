import telebot
from dotenv import load_dotenv
from sound import *
from functions import *
from slowars import *

from functions import screen
load_dotenv()
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))



@bot.message_handler()
def starter(message):
    # скріншот
    for command in screenshot:
        if command in message.text:
            screen()

    for command in command_slowar:
        if command in message.text:
            open_command_slowar("command")

    # чат ГПТ
    for command in znach:
        if command in message.text:
            open()
            url = "https://chat.openai.com/"
            webbrowser.open(url)

    # повертає назад вкладку в гуглі
    for command in res_wkl_0:
        if command in message.text:
            res_wkl()

    # закрийває вкладку
    for command in close_wkl_0:
        if command in message.text:
            close_wkl()

    # відкриває нову вкладку
    for command in open_wkl_0:
        if command in message.text:
            open_wkl()

    # закриває все(Alt+f4)
    for command in close_0:
        if command in message.text:
            close()

    # звертає поточну програму
    for command in zverni_0:
        if command in message.text:
            zverni()

    # вимокає/вмикає звук
    for command in valume_on_off_0:
        if command in message.text:
            valume_on_off()

    # запис відео
    for command in scr_video:
        if command in message.text:
            scr_videos()

    # вимокає/вмикає мікрофон
    for command in micro_0:
        if command in message.text:
            micro()

    for command in up:
        if command in message.text:
            upi()

    for command in down:
        if command in message.text:
            downi()

    # для пошуку у ПК
    for command in comp_slowar:
        if command in message.text:
            open()
            result = message.text.replace(command, '')
            result = result.title()
            result = result.strip()
            print(result)
            open_item_on_desktop(result)

    if "Припини роботу" in message.text:
        flag = 2
        see_you()
        sys.exit()
    if 'Сплячий режим' in message.text or 'Спящий режим' in message.text or 'сплячий режим' in message.text or 'спящий режим' in message.text:
        dont_listen()

    if flag == 0:
        UnknownComand()




bot.polling(none_stop=True)