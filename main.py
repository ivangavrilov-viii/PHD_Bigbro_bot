from telebot.types import Message, CallbackQuery
from init.class_user import BotUser
from init.messages import *
from init.db_funcs import *
from decouple import config
from typing import Dict
import telebot


bot = telebot.TeleBot(config('phd_bot'))
users_dict: Dict[int, BotUser] = dict()
admin_list = [462841846, 2010916504]


@bot.message_handler(content_types=['text'])
def start(message: Message) -> None:
    """ Call and process basic bot commands """

    global users_dict
    user_chat_id = message.chat.id
    users_dict[user_chat_id] = create_user(message.chat, BotUser(message.chat))
    users_dict[user_chat_id] = BotUser(message.chat)

    if message.text == '/email':
        bot.send_message(user_chat_id, email_message())
        bot.register_next_step_handler(message, enter_email)
    elif message.text == '/team':
        bot.send_message(user_chat_id, text=team_message(), reply_markup=team_keyboard())
    elif message.text == '/help':
        bot.send_message(user_chat_id, function_list(user_chat_id))
    elif message.text == '/users' and user_chat_id in admin_list:
        bot.send_message(user_chat_id, get_users())
        send_users_list(message)
    elif message.text == '/start':
        bot.send_message(user_chat_id, start_message(message))
        bot.send_message(user_chat_id, email_message())
        bot.register_next_step_handler(message, enter_email)
    else:
        bot.send_message(user_chat_id, function_list(user_chat_id))


def enter_email(message):
    """ UPDATE EMAIL FOR USER """

    user_email = message.text
    user_id = message.chat.id
    user = users_dict[user_id]

    if user_email.startswith('/'):
        bot.send_message(user_id, function_list(user_id))
    else:
        try:
            user.email = user_email
            success = update_email(message.chat, user)
            if success:
                bot.send_message(user_id, text=team_message(), reply_markup=team_keyboard())
            else:
                bot.send_message(user_id, 'Введенный email не соответствует необходимому формату...\nПопробуйте снова')
                bot.register_next_step_handler(message, enter_email)
        except Exception as error:
            logger.error(f"Wrong input email = {user_email} by {user}. Error: {error}")
            bot.send_message(user_id, 'Введенный email не соответствует необходимому формату...\nПопробуйте снова')
            bot.register_next_step_handler(message, enter_email)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call: CallbackQuery) -> None:
    """ UPDATE TEAM FOR USER IN DB """

    user_id = call.message.chat.id
    user = users_dict[user_id]
    user_team = call.data

    try:
        user.team = user_team
        success = update_team(call.message.chat, user)
        if success:
            end_success(user_id)
        else:
            bot.send_message(user_id, 'Данного варианта нет предложенном списке...\nПопробуйте снова')
            bot.send_message(user_id, text=team_message(), reply_markup=team_keyboard())
    except Exception as error:
        logger.error(f"Wrong input team = {user_team} by {user}. Error: {error}")
        bot.send_message(user_id, 'Данного варианта нет предложенном списке...\nПопробуйте снова')
        bot.send_message(user_id, text=team_message(), reply_markup=team_keyboard())


def end_success(user_id):
    """ SAVE USER'S DATA IN GOOGLE SHEETS """

    user = check_user_in_db(user_id)
    user = user[0] if user and user[0] else None
    if user:
        bot.send_message(user_id, success_mesage())


def send_users_list(message):
    user_id = message.chat.id
    users_list = get_all_user()

    with open('users.txt', 'w+', encoding='utf-8') as file:
        for user in users_list:
            file.write(f"{user[0]} {user[1]} {user[2]} {user[3]} {user[4]} {user[5]}\n")
        file.close()

    bot.send_document(user_id, open('users.txt', 'rb'))


if __name__ == '__main__':
    logger.add('logger.log', level='DEBUG', format='{time} {level} {message}', encoding='utf-8')
    bot.polling(none_stop=True, interval=0)
