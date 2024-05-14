import ctypes

def get_current_keyboard_layout():
    user32 = ctypes.windll.user32
    hkl = user32.GetKeyboardLayout(0)
    lang_id = hkl & 0xFFFF
    return lang_id

def switch_to_english_layout():
    current_layout = get_current_keyboard_layout()
    if current_layout != 0x0409:  # Код 0x0409 відповідає англійській мові
        user32 = ctypes.windll.user32
        user32.LoadKeyboardLayoutW("00000409", 1)  # Змінюємо розкладку на англійську

# Викликаємо функцію для перевірки та зміни розкладки на англійську
switch_to_english_layout()