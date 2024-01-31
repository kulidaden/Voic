import webbrowser

from importings import *

def search_query(query):
    url = f"https://bing.com/search?q={query}"
    webbrowser.open(url)


def search_in_youtube(text,command):
    result = text.replace(command, '')
    url = "https://www.youtube.com/results?search_query=" + '+' + result
    webbrowser.open(url)

def search_in_google(text,command):
    result1 = text.replace(command, '')
    url = "https://bing.com/search?q=" + '+' + result1
    search_results = list(search(url, num_results=10, lang='uk'))
    webbrowser.open(url)


#підключення до БД
conn=sqlite3.connect('DataBase_V\\test.db',check_same_thread=False)

#для пошуку у ПК
def open_item_on_desktop(item_name,command):
    item_name = item_name.replace(command, '')
    item_name = item_name.strip()
    item_name=item_name.title()
    print(1)
    cursor = conn.cursor()
    print(2)
    cmd_way = f'SELECT way FROM program WHERE name="{item_name}"'
    print(3)
    cursor.execute(cmd_way)
    print(4)
    result = cursor.fetchone()
    print(5)
    if result:
        print(result)
        program_path = result[0]  # Отримання шляху з результату запиту
        zak = ['.lnk', '.exe', '.xlsx', '.txt', '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.mp3', '.mp4', '.docx']

        file_path = None
        for i in zak:
            current_path = f'{program_path}\\{item_name}{i}'

            if os.path.exists(current_path):
                file_path = current_path
                print(current_path)
                break  # Вийти з циклу, якщо знайдено файл
            else:
                current_path=f"{program_path}\\{item_name}"
                if os.path.exists(current_path):
                    file_path=current_path
                    break

        if file_path:
            try:
                os.startfile(file_path)
                print(f"Відкрито програму: {file_path}")
            except Exception as e:
                print(f"Помилка при відкритті програми: {e}")
        else:
            print("Файл не знайдено")
    else:
        print("НЕ ЗНАЙШОВ У БД")
        item_name = item_name.strip().title()
        taskbar_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Internet Explorer', 'Quick Launch', 'User Pinned', 'TaskBar')
        main_desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        public_desktop_path = os.path.join(os.path.join(os.environ['PUBLIC']), "Desktop")
        desktop_paths = [main_desktop_path, public_desktop_path, taskbar_path, 'D:\\', 'C:\\']
        for desktop_path in desktop_paths:
            if os.path.exists(desktop_path):
                for root, dirs, files in os.walk(desktop_path):
                    for current_item_name in files + dirs:
                        current_item_path = os.path.join(root, current_item_name)
                        try:
                            current_item_name_without_extension, current_item_extension = os.path.splitext(current_item_name.strip())
                            if current_item_name_without_extension.lower() == item_name.lower():
                                if current_item_extension.lower() == '.lnk':
                                    shell = win32com.client.Dispatch("WScript.Shell")
                                    shortcut = shell.CreateShortCut(current_item_path)
                                    item_to_open = shortcut.Targetpath
                                else:
                                    item_to_open = current_item_path
                                if os.path.isdir(item_to_open) or current_item_extension.lower() in (
                                        '.lnk', '.exe', '.xlsx', '.txt', '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.mp3', '.mp4', '.docx'):
                                    os.startfile(item_to_open)
                                    # Вставляйте в базу даних лише в разі успішного відкриття
                                    cmd1 = f'''INSERT INTO program (name, way) VALUES ('{item_name}','{root}')'''
                                    conn.execute(cmd1)
                                    conn.commit()
                                    print(f"Відкрито {item_name} з робочого столу.")
                                    return
                                elif os.path.isdir(item_to_open) or current_item_extension.lower():
                                    os.startfile(item_to_open)
                                    cmd1 = f'''INSERT INTO program (name, way) VALUES ('{item_name}','{root}')'''
                                    conn.execute(cmd1)
                                    conn.commit()
                                    print(f"Відкрито {item_name} з робочого столу.")
                                    return
                                else:
                                    print(f"Не вдається визначити тип {item_name}.")
                                    return
                        except Exception as e:
                            print(f"Помилка відкриття {item_name}: {e}")
        print(f"{item_name} не знайдено на робочому столі або в директоріях C або D.")
#сплячий режим

def dont_listen(nothing):
    recognizer = sr.Recognizer()
    sl_for_get_up = ['проснись', 'Проснись', 'прокинься', 'Прокинься', 'повернувся', 'Повернувся',
           'вернувся','Вернувся','очнись','Очнись',]

    with sr.Microphone() as source:
        print("Скажіть що-небудь...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="uk-UA")
        print(f"Розпізнанний текст: {text}")

        for i in sl_for_get_up:
            if i in text:
                print('всьо')
                break
        else:
            print("повтор1")
            dont_listen()  # Рекурсивний виклик, якщо жодного ключового слова не виявлено

    except Exception as e:
        print(f"Помилка: {e}")
        print("повтор2")
        dont_listen()

#повертає вкладку
def res_wkl(nothing):
    keyboard.press_and_release('ctrl+shift+t')
#закриває вкладку
def close_wkl(nothing):
    keyboard.press_and_release('ctrl+w')
#відкриває нову вкладку
def open_wkl(nothing):
    keyboard.press_and_release('ctrl+t')
#закриває поточну програму
def close(nothing):
    keyboard.press_and_release('alt+f4')
#звертає поточну програму
def zverni(nothing):
    keyboard.press_and_release('left windows+d')

#запис відео
def scr_videos(nothing):
    keyboard.press_and_release('win+alt+r')

#вкл\викл мікро
def micro(nothing):
    keyboard.press_and_release('win+alt+m')

#робить скрін
# def screen():
#     times=datetime.now().strftime("%Y%m%d%H%M%S")
#     name_file=f'знімок_{times}.png'
#     scr=pyautogui.screenshot()
#     scr.save(f'screenshots/{name_file}')

def screen(nothing):
    keyboard.press_and_release('print screen')


#вимокає/вмикає звук
mute_state = False
def valume_on_off(nothing):
    global mute_state

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Зміна стану вимкнення/ввімкнення звуку
    mute_state = not mute_state

    # Встановлення стану вимкнення/ввімкнення звуку
    volume.SetMute(mute_state, None)

def read_list_from_file(file_path):
    result_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            result_list.append(line.strip())
    return result_list

def chat_gpt(nothing):
    webbrowser.open("https://chat.openai.com/")
def open_command_slowar(file='command'):
    try:
        os.startfile(file)
    except Exception as e:
        print(f"Сталася помилка: {e}")

def upi(nothing):
    pyautogui.scroll(500)

def downi(nothing):
    pyautogui.scroll(-500)





















#
#
# def open_folder(folder_path):
#     try:
#         # Відкрити папку за допомогою системного застосунку за замовчуванням
#         os.startfile(folder_path)  # Цей метод працює тільки на Windows
#
#         # Якщо ви використовуєте macOS, ви можете скористатися:
#         # os.system('open "{}"'.format(folder_path))
#
#         # Якщо ви використовуєте Linux, ви можете скористатися:
#         # os.system('xdg-open "{}"'.format(folder_path))
#
#         print(f"Папка {folder_path} відкрита успішно.")
#     except Exception as e:
#         print(f"Сталася помилка: {e}")
#
# # Задайте шлях до папки, яку ви хочете відкрити
# folder_path = r'C:\\Users\\Denis\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'  # Замініть це на шлях до вашої папки
#
# # Викликати функцію для відкриття папки
# open_folder(folder_path)
