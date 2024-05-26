from datetime import datetime
from telebot import types


admin_list = [462841846, 2010916504]

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
        return f'Приветствуем Вас, {message.chat.first_name}!\nЭто бот PHD&Bigbro.ai\n\nЧтобы получить видео-аналитику игроков своей команды - необходимо ввести почту, на которую мы её сможем отправить!\n\nБолее подробную информацию о видео-аналитике и как это устроено вы сможете на сайте bigbro.ai'
    return f'Приветствуем Вас!\nЭто бот PHD&Bigbro.ai\n\nЧтобы получить видео-аналитику игроков своей команды - необходимо ввести почту, на которую мы её сможем отправить!\n\nБолее подробную информацию о видео-аналитике и как это устроено вы сможете на сайте bigbro.ai'


def function_list(user_id) -> str:
    if user_id in admin_list:
        return (f'Вы можете воспользоваться командами:\n'
                f'/users — Получить список всех пользователей\n'
                f'/help — Список возможных команд\n'
                f'/email — Изменить Ваш email\n'
                f'/team -  Изменить название Вашей команды\n')
    return (f'Вы можете воспользоваться командами:\n'
            f'/help — Список возможных команд\n'
            f'/email — Изменить Ваш email\n'
            f'/team -  Изменить название Вашей команды\n')


def email_message() -> str:
    return f"Введите Вашу электронную почту: "


def team_message() -> str:
    return f"Выберите название Вашей команды из списка: "


def success_mesage() -> str:
    return f"Спасибо!\nВ ближайшее время на указанную почту мы пришлем необходимую информацию."


def team_success() -> str:
    return f'Ваша команда успешно изменена!'


def team_keyboard() -> types.InlineKeyboardMarkup:
    """ CREATE KEYBAORD FOR TEAM LIST """

    keyboard = types.InlineKeyboardMarkup()
    for team in team_list:
        keyboard.add(types.InlineKeyboardButton(text=team['name'], callback_data=team['key']))
    return keyboard


def get_users() -> str:
    return f'Список всех пользователей телеграм-бота:'
