<p align="center">
  <img width="450px" height='250px' src="./teleBot.png" align="center" alt="Telegram_Bot" />
  <h2 align="center">🤖Telegram Bot🤖</h2>
</p>
Тут ви можете використовувати телеграм бота в якості помічника з дистанційного керування комп'ютором. Для цього достатньо зайти в телеграм(з телефону, наприклад), написати, що вам потрібно(типу відкрий Telegram) і він це зробить, поки ви йдете до своєї кімнати.

# Інсталяція
1. Клонуйте репозиторій: `git clone https://github.com/kulidaden/Voic.git`;
2. Зайдіть в папку 'Voic';
3. Створіть віртуальне середовище та активуйте його;
4. Потрібно зайти в телеграм, та знайти чат з @BotFather та написати наступно команду: `/newbot`;
5. Даєте назву боту;
7. Даєте другу назву боз з закінчкнням `_bot`;
8. Скопіюйте з повідомлення ключ(наприклад: `2456437531:AAG3vho73s6fxyTbQlHhyuXwFtnj22OlZs`);
9. Тепер вам потрібно знайти другий чат бот для того щоб знати свій ID, тут пишемо боту @useridinfobot команду /start і отримуємо ID;
11. Будучи у папці Voic створіть перший exe файл для введення ключа і ID у базу даних, написавши команду `pyinstaller --onefile --distpath ./ key_for_tg.py`;
12. Тепер запустіть його командою `./key_for_tg.exe`;
13. Вставте отриманий ключ та ID;
15. Створіть основний exe файл: `pyinstaller --onefile --distpath ./ osnova.py`
16. Запустіть його: `./osnova.exe`
   
## Використання
Після запуску вам прийде повідомлення від бота, щоб ви його не шукали. Тепер ви можете йому писати свої команди.

## Контакт
Якщо Вам потрібна консультація або допомога по використанні програми: Telegram: @DeLemse

##

<p align="center">
  <img width="450px" height='250px' src="./teleBot.png" align="center" alt="Telegram_Bot" />
  <h2 align="center">🤖Telegram Bot🤖</h2>
</p>
Here you can use the Telegram bot as an assistant for remote computer control.  To do this, it is enough to go to Telegram, write what you need (like open Telegram) and he will do it while you go to your room.

# Installation
1. Clone the repository: `git clone https://github.com/kulidaden/Voic.git`;
2. Go to the 'Voic' folder;
3. Create a virtual environment and activate it;
4. You need to go to Telegram and find the chat with @BotFather and write the following command: `/newbot`;
5. Give the name of the bot;
7. Give the bot a second name ending in `_bot';
8. Copy the key from the message (for example: `7256435231:AAG3vTo73s6fx3TbQlHHMgCXwFtnj22OlZs`);
9. Now you need to find a second chat bot in order to know your ID, here we write the `/start` command to the @useridinfobot bot and get the ID;
11. Being in the Voic folder, create the first exe file for entering the key and ID into the database by writing the command `pyinstaller --onefile --distpath ./ key_for_tg.py`;
12. Now run it with the command `./key_for_tg.exe`;
13. Insert the received key and ID;
15. Create the main exe file: `pyinstaller --onefile --distpath ./ base.py`;
16. Run it: `./osnova.exe`;
   
## Usage
After launch, you will receive a message from the bot so that you do not look for it.  Now you can write your commands to it.

## Contact
If you need advice or help using the program: Telegram: @DeLemse
