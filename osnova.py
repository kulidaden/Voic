import time

import keyboard
from sound import *
from functions import *
from slowars import *
from telebot import types
import speech_recognition as sr
recognizer = sr.Recognizer()
load_dotenv()
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

def mu():
    @bot.message_handler(func=lambda message: True)
    def starter(message):
        markup = types.ReplyKeyboardMarkup()
        close_prog = types.KeyboardButton("Закрити")
        telegramchiK = types.KeyboardButton('Telegram')
        command_list = types.KeyboardButton('Список команд')
        markup.row(close_prog, telegramchiK,command_list)
        bot.send_message(message.chat.id, 'do', reply_markup=markup)
        global result1
        global search_results
        try:
            print(f"Розпізнанний текст: {message.text.lower()}")
            flag = 0
            list_of_commands = {'command\\пошук_ютуб.txt': search_in_youtube,
                                'command\\чат_gpt.txt': chat_gpt,
                                'command\\пошук_гугл.txt': search_in_google,
                                'command\\запис_екрану.txt': scr_videos,
                                "command\\мікрофон.txt": micro,
                                "command\\пов_закр_вкладок.txt": res_wkl,
                                "command\\закрити_вкладку.txt": close_wkl,
                                "command\\нові_вкладки.txt": open_wkl,
                                "command\\закрити_пот_програму.txt": close,
                                "command\\звренення_програми.txt": zverni,
                                "command\\вкл_викл_звуку.txt": valume_on_off,
                                "command\\знімок_екрану.txt": screen,
                                'command\\вижче.txt': upi,
                                'command\\нижче.txt': downi,
                                "command\\зпуск_програм.txt":open_item_on_desktop}
            for i in list_of_commands:
                for command in read_list_from_file(i):
                    if command in message.text:
                        list_of_commands[i](message.text,command)
                        flag = 1
                        break

            if message.text == 'Закрити':
                keyboard.press_and_release("alt+f4")
                flag=1
            elif message.text == 'Telegram':
                open_item_on_desktop("Telegram",command)
                flag=1
            elif message.text == 'Список команд':
                open_command_slowar()
                flag=1
            if flag == 0:
                UnknownComand()
        except sr.UnknownValueError:
            dontUnderstedebl()
        except sr.RequestError as e:
            print(f"Ошибка при запросе к Google Web Speech API: {e}")

    bot.polling(none_stop=True)
mu()
