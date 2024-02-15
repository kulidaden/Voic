import sqlite3
import time
import keyboard
import pygame
from sound import *
from functions import *
from slowars import *
from telebot import types
import speech_recognition as sr
recognizer = sr.Recognizer()
load_dotenv()
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
conn=sqlite3.connect("DataBase_V\\test.db", check_same_thread=False)

def mu():
    @bot.message_handler(func=lambda message: True)
    def starter(message):
        flag = 0
        def do_command():
            file_path = open_command_slowar('command')
            for file in file_path:
                for command in read_list_from_file(file):
                    if command in message.text:
                        Foo(message.text, command, file)
                        flag = 1
                        break
        #перші інлайни
        markup_first = types.ReplyKeyboardMarkup()
        list_for_inl = ['Закрити❌', 'Музика🎧','Вкл звук🔊', 'Звернути⭕️', 'Інтернет🌐','Викл звук🔇', 'Програми🖥','Викл Музику🚫🎧']
        for i in range(0, len(list_for_inl), 3):
            rows=[types.KeyboardButton(button) for button in list_for_inl[i:i+3]]
            markup_first.row(*rows)
        bot.send_message(message.chat.id,'do',reply_markup=markup_first)


        #інлайни музики
        if message.text == 'Музика🎧':
            markup_music=types.ReplyKeyboardMarkup()
            list_for_music=[i for i in open_command_slowar('музика')]
            for i in range(0,len(list_for_music), 3):
                row=[types.KeyboardButton(mus_button) for mus_button in list_for_music[i:i+3]]
                markup_music.row(*row)
            bot.send_message(message.chat.id, 'music', reply_markup=markup_music)
            flag=1

        #інтернет інлайни
        elif message.text == 'Інтернет🌐':
            markup_serch = types.ReplyKeyboardMarkup()
            curssor = conn.cursor()
            curssor.execute('SELECT name FROM links')
            res = curssor.fetchall()
            print(res)
            names = ['l'+row[0] for row in res]
            for i in range(0, len(names), 3):
                rows = [types.KeyboardButton(button) for button in names[i:i + 3]]
                markup_serch.row(*rows)
            bot.send_message(message.chat.id, 'searcher', reply_markup=markup_serch)

        #програмні інлайни
        elif message.text == 'Програми🖥':
            markup_prog=types.ReplyKeyboardMarkup()
            list_for_programs=[]
            cursor = conn.cursor()
            cmd_way = 'SELECT name FROM program'
            cursor.execute(cmd_way)
            result = cursor.fetchall()
            for row in result:
                list_for_programs.append(row[0])
            print(list_for_programs)
            for i in range(0, len(list_for_programs),4):
                rows=[types.KeyboardButton('Відкрити '+button) for button in list_for_programs[i:i+4]]
                markup_prog.row(*rows)
            bot.send_message(message.chat.id, 'programs', reply_markup=markup_prog)

        else:
            try:
                print(f'Розпізнаний текст: {message.text}')
                for i in list_for_inl:
                    if message.text in i:
                        do_command()
                        break
                    flag=1
                else:
                    do_command()
                    flag=1
                if flag == 0:
                    bot.send_message(message.chat.id, 'Unknown command')
            except sr.UnknownValueError:
                dontUnderstedebl()
            except sr.RequestError as e:
                print(f"Ошибка при запросе к Google Web Speech API: {e}")

    bot.polling(none_stop=True)
mu()
