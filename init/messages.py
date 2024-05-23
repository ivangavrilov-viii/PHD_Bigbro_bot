from datetime import datetime
from telebot import types


team_list = [
    {'name': 'Positive Technologies', 'key': 'Positive Technologies'},
    {'name': 'Тинькофф', 'key': 'Тинькофф'},
    {'name': 'VK', 'key': 'VK'},
    {'name': 'Kaspersky', 'key': 'Kaspersky'},
    {'name': 'Solar', 'key': 'Solar'},
    {'name': 'Solar 2', 'key': 'Solar 2'},
    {'name': 'Банк России', 'key': 'Банк России'},
    {'name': 'КРОК', 'key': 'КРОК'},
]


def start_message(message) -> str:
    if message.chat.first_name is not None:
        return f'Здравствуйте, {message.chat.first_name} 👋\n' \
               f'Это бот Bigbro.io\n'
    return f'Здравствуйте 👋\n' \
           f'Это бот Bigbro.io\n'


def function_list() -> str:
    return (f'Вы можете воспользоваться командами:\n'
            f'/email — Изменить Ваш email\n'
            f'/team -  Изменить название Вашей команды\n')


def email_message() -> str:
    return f"Введите Вашу электронную почту: "


def team_message() -> str:
    return f"Выберите название Вашей команды из списка: "


def success_mesage() -> str:
    return f"Ваши данные успешно сохранены!\nМы с Вами свяжемся по окончании турнира"


def team_keyboard() -> types.InlineKeyboardMarkup:
    """ CREATE KEYBAORD FOR TEAM LIST """

    keyboard = types.InlineKeyboardMarkup()
    for team in team_list:
        keyboard.add(types.InlineKeyboardButton(text=team['name'], callback_data=team['key']))
    return keyboard
