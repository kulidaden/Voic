import keyboard
from importings import *
import pygame.mixer
import webbrowser
import pythoncom
import requests
from bs4 import BeautifulSoup
import pyautogui

conn = sqlite3.connect('DataBase_V\\test.db', check_same_thread=False)

class Foo:
    def __init__(self, message, command, file):
        self.message=message
        self.command=command
        self.file=file
        self.listFoo()

    def open_item_on_desktop(self, message, command):
        message = message.replace(command, '').strip()
        print(message)
        pythoncom.CoInitialize()

        cursor = conn.cursor()
        cmd_way = f'SELECT way FROM program WHERE name="{message}"'
        cursor.execute(cmd_way)
        result = cursor.fetchone()

        if result:
            program_path = result[0]  # Отримуємо шлях з результату запиту

            zak = ['.lnk', '.exe', '.xlsx', '.txt', '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.mp3',
                   '.mp4', '.docx','.pdf','.bat','.sh','.app','.jar','.doc','.rtf','.odt','.xls',
                   '.csv','.ods','.ppt','.pptx','.odp','.tiff','.svg','.wav','.flac','.aac','.yaml',
                   '.ogg','.avi','.mkv','.mov','.wmv','.zip','.rar','.tar','.gz','.7z','.json','.otf'
                   '.py','.java','.cpp','.cs','.js','.html','.css','.ini','.cfg','.conf','.xml',
                   '.yml','.sys','.dll','.drv','.dmg','.db','.sql','.mdb','.sqlite','.ttf','.woff',
                   '.htm','.php','.asp','.iso','.md','.log','.bak','.tmp']
            file_path = None
            for i in zak:
                current_path = os.path.join(program_path, f'{message}{i}')
                if os.path.exists(current_path):
                    file_path = current_path
                    break  # Вийти з циклу, якщо знайдено файл
                else:
                    current_path = os.path.join(program_path, message)
                    if os.path.exists(current_path):
                        file_path = current_path
                        break

            if file_path:
                try:
                    os.startfile(file_path)
                    print(f"Відкрито програму: {file_path}")
                except Exception as e:
                    print(f"Помилка при відкритті програми: {e}")
            else:
                print("Файл не знайдено в базі даних111")
        else:
            print("Програму не знайдено в базі даних")

            taskbar_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Internet Explorer', 'Quick Launch',
                                        'User Pinned', 'TaskBar')
            main_desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            public_desktop_path = os.path.join(os.environ['PUBLIC'], "Desktop")
            desktop_paths = [main_desktop_path, taskbar_path, public_desktop_path, 'D:\\', 'C:\\']

            for desktop_path in desktop_paths:
                if os.path.exists(desktop_path):
                    for root, dirs, files in os.walk(desktop_path):
                        for current_item_name in files + dirs:
                            current_item_path = os.path.join(root, current_item_name)
                            try:
                                print(current_item_path)
                                current_item_name_without_extension, current_item_extension = os.path.splitext(
                                    current_item_name.strip())
                                if current_item_name_without_extension.lower() == message.lower():
                                    if current_item_extension.lower() == '.lnk':
                                        shell = win32com.client.Dispatch("WScript.Shell")
                                        shortcut = shell.CreateShortCut(current_item_path)
                                        item_to_open = shortcut.Targetpath
                                    else:
                                        item_to_open = current_item_path

                                    if os.path.isfile(item_to_open):
                                        os.startfile(item_to_open)
                                        cmd1 = f'''INSERT INTO program (name, way) VALUES ('{message}','{root}')'''
                                        conn.execute(cmd1)
                                        conn.commit()
                                        print(f"Відкрито {message} з робочого столу.")
                                        return
                                    else:
                                        print(f"Не вдається відкрити {message}. Файл не знайдено.")
                                        return
                            except Exception as e:
                                print(f"Помилка відкриття {message}: {e}")
            print(f"{message} не знайдено на робочому столі або в директоріях C або D.")

    def search_in_youtube(self,message, command):
        curssor=conn.cursor()
        curssor.execute('DELETE FROM links;')
        res=curssor.fetchall()
        result1 = message.replace(command, '')
        print(result1)
        url = "https://www.youtube.com/results?search_query=" + '+' + result1
        search_results = list(search(url, num_results=10, lang='uk'))
        for link in search_results:
            print("Посилання:", link)
            try:
                response = requests.get(link)
                soup = BeautifulSoup(response.text, 'html.parser')
                text_under_link = soup.get_text().strip()
                if text_under_link.strip():
                    print("Текст під посиланням:", text_under_link[:60])
                    ins_url_name=(f'''INSERT INTO links (url, name) VALUES ('{link}','{text_under_link[:60]}') ''')
                    conn.execute(ins_url_name)
                    conn.commit()

            except Exception as e:
                print("Не вдалося зчитати текст під посиланням:", e)
        webbrowser.open(url)
        result1 = result1
        print(result1)

    def search_in_google(self,message, command):
        curssor=conn.cursor()
        curssor.execute('DELETE FROM links;')
        res=curssor.fetchall()
        result1 = message.replace(command, '')
        print(result1)
        url = "https://www.google.com/search?q=" + '+' + result1
        search_results = list(search(url, num_results=10, lang='uk'))
        for link in search_results:
            print("Посилання:", link)
            try:
                response = requests.get(link)
                soup = BeautifulSoup(response.text, 'html.parser')
                text_under_link = soup.get_text().strip().replace(' ','')
                text_under_link = text_under_link.replace('\n','')
                if text_under_link.strip():
                    print("Текст під посиланням:", text_under_link[:60])
                    ins_url_name=(f'''INSERT INTO links (url, name) VALUES ('{link}','{text_under_link[:60]}') ''')
                    conn.execute(ins_url_name)
                    conn.commit()

            except Exception as e:
                print("Не вдалося зчитати текст під посиланням:", e)
        webbrowser.open(url)
        result1 = result1
        print(result1)
    conn = sqlite3.connect('DataBase_V\\test.db', check_same_thread=False)

    def l(self, message, command):  # Передайте з'єднання як аргумент
        message = message.replace(command, "")
        self.message = message.replace(' ','')
        print(self.message,1)
        cursor = conn.cursor()
        cmd_url = 'SELECT url FROM links WHERE name=?'  # Використовуйте параметризований запит
        print(cmd_url,2)
        cursor.execute(cmd_url, (self.message,))
        print(3)
        print(cursor)
        print(4)
        res = cursor.fetchone()
        print(5)
        print(res,6)
        print(7)
        if res:  # перевірка, чи результат існує
            res = res[0]  # перетворення кортежу на рядок
            res = res.translate(str.maketrans('', '', '()\'"'))  # видалення дужок та лапок
            print(res,8)
            webbrowser.open(res)
        else:
            print("URL not found",9)

    def res_wkl(self):
        keyboard.press_and_release('ctrl+shift+t')

    # закриває вкладку
    def close_wkl(self):
        keyboard.press_and_release('ctrl+w')

    # відкриває нову вкладку
    def open_wkl(self):
        keyboard.press_and_release('ctrl+t')

    # закриває поточну програму
    def close(self):
        keyboard.press_and_release('alt+f4')

    # звертає поточну програму
    def zverni(self):
        try:
            keyboard.press_and_release('left windows+d')
        except:
            keyboard.press_and_release('left windows+в')

    # запис відео
    def scr_videos(self):
        keyboard.press_and_release('win+alt+r')

    # вкл\викл мікро
    def micro(self):
        keyboard.press_and_release('win+alt+m')

    def screen(self):
        keyboard.press_and_release('print screen')

    def valume_on(self):
        mute_state = 50
        comtypes.CoInitialize()
        devices = AudioUtilities.GetSpeakers()
        if devices:
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            mute_state = not mute_state
            volume.SetMute(mute_state, None)
        else:
            print("Не вдалося знайти пристрій виведення звуку.")

    def valume_off(self):
        mute_state = False
        comtypes.CoInitialize()
        devices = AudioUtilities.GetSpeakers()
        if devices:
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            mute_state = not mute_state
            volume.SetMute(mute_state, None)
        else:
            print("Не вдалося знайти пристрій виведення звуку.")

    def chat_gpt(self,name='чат_gpt.txt'):
        webbrowser.open("https://chat.openai.com/")

    def upi(self,name='вижче.txt'):
        pyautogui.scroll(500)

    def downi(self,name='нижче.txt'):
        pyautogui.scroll(-500)

    def music(self):
        try:
            pygame.mixer.stop()
            pygame.init()
            sound = pygame.mixer.Sound(f"музика\\{self.message}.mp3")
            sound.play()
        except:
            pygame.init()
            sound = pygame.mixer.Sound(f"музика\\{self.message}.mp3")
            sound.play()

    def stop_music(self):
        try:
            pygame.mixer.stop()
        except:
            pass
    def listFoo(self):
        list_for_SCH_inPC = [self.open_item_on_desktop]

        list_for_Searc_in_Internet = [self.search_in_youtube, self.search_in_google, self.l]

        list_for_keyboard = [self.close, self.res_wkl, self.screen, self.scr_videos,self.open_wkl,self.close_wkl,
                             self.zverni, self.micro, self.valume_on,self.valume_off, self.upi,
                             self.downi, self.chat_gpt,self.music,self.stop_music]
        txt = '.txt'
        for item in list_for_SCH_inPC:
            self.file=self.file.replace(txt, '')
            if item.__name__==self.file:
                print(item.__name__,'файл= '+self.file)
                self.open_item_on_desktop(self.message,self.command)
                break
        for item in list_for_Searc_in_Internet:
            self.file=self.file.replace(txt, '')
            if item.__name__==self.file:
                print(item.__name__,'файл= '+self.file)
                item(self.message,self.command)
                break
        for item in list_for_keyboard:
            self.file=self.file.replace(txt, '')
            if item.__name__==self.file:
                print(item.__name__,'файл= '+self.file)
                item()
                break




def read_list_from_file(file_path):
    result_list = []
    pathhs = 'command\\' + file_path
    with open(pathhs, 'r', encoding='utf-8') as file:
        for line in file:
            result_list.append(line.strip())
    return result_list


def open_command_slowar(folder_path):
    try:
        files_in_folder = os.listdir(folder_path)
        return files_in_folder
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []


























#
#
# # file_path = open_command_slowar()
# # for file in file_path:
# #     for item in read_list_from_file(file):
# #         print(item)
# #сплячий режим
#     # def dont_listen(self,nothing,name):
#     #     recognizer = sr.Recognizer()
#     #     sl_for_get_up = ['проснись', 'Проснись', 'прокинься', 'Прокинься', 'повернувся', 'Повернувся',
#     #            'вернувся','Вернувся','очнись','Очнись',]
#     #
#     #     with sr.Microphone() as source:
#     #         print("Скажіть що-небудь...")
#     #         audio = recognizer.listen(source)
#     #
#     #     try:
#     #         text = recognizer.recognize_google(audio, language="uk-UA")
#     #         print(f"Розпізнанний текст: {text}")
#     #
#     #         for i in sl_for_get_up:
#     #             if i in text:
#     #                 print('всьо')
#     #                 break
#     #         else:
#     #             print("повтор1")
#     #             dont_listen()  # Рекурсивний виклик, якщо жодного ключового слова не виявлено
#     #
#     #     except Exception as e:
#     #         print(f"Помилка: {e}")
#     #         print("повтор2")
#     #         dont_listen()
#
# #
# #
# # def open_folder(folder_path):
# #     try:
# #         # Відкрити папку за допомогою системного застосунку за замовчуванням
# #         os.startfile(folder_path)  # Цей метод працює тільки на Windows
# #
# #         # Якщо ви використовуєте macOS, ви можете скористатися:
# #         # os.system('open "{}"'.format(folder_path))
# #
# #         # Якщо ви використовуєте Linux, ви можете скористатися:
# #         # os.system('xdg-open "{}"'.format(folder_path))
# #
# #         print(f"Папка {folder_path} відкрита успішно.")
# #     except Exception as e:
# #         print(f"Сталася помилка: {e}")
# #
# # # Задайте шлях до папки, яку ви хочете відкрити
# # folder_path = r'C:\\Users\\Denis\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'  # Замініть це на шлях до вашої папки
# #
# # # Викликати функцію для відкриття папки
# # open_folder(folder_path)
#
#
# # def search_query(self,query,name):
# #     url = f"https://bing.com/search?q={query}"
# #     webbrowser.open(url)