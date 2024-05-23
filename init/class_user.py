from telebot.types import Chat
from datetime import datetime


class BotUser:
    """ Class: Telegram bot's user """

    def __init__(self, chat: Chat) -> None:
        self.first_name = chat.first_name
        self.last_name = chat.last_name
        self.username = chat.username
        self.user_id = chat.id
        self.email = str()
        self.team = str()

    def __str__(self) -> str:
        return (f'First name: {self.first_name}, Last name: {self.last_name}, User ID: {self.user_id}, '
                f'Username: @{self.username}\n Email: {self.email}\n Team: {self.team}')
