from loguru import logger
import sqlite3


db_name = 'bot_db.db'


def update_email(chat, bot_user_class):
    """ UPDATE EMAIL IN DB """

    try:
        table = sqlite3.connect(db_name)
        cursor = table.cursor()
        cursor.execute(f"UPDATE users SET email = ? WHERE user_id = ?", (bot_user_class.email, bot_user_class.user_id))
        table.commit()
        cursor.close()
        # logger.info(f'SUCCESS | EMAIL WAS UPDATED FOR USER(#{bot_user_class.user_id}).')
        return True
    except sqlite3.Error as error:
        logger.error(f'ERROR | Error with database {error}')
    return False


def update_team(chat, bot_user_class):
    """ UPDATE TEAM IN DB """

    try:
        table = sqlite3.connect(db_name)
        cursor = table.cursor()
        cursor.execute(f"UPDATE users SET team = ? WHERE user_id = ?", (bot_user_class.team, bot_user_class.user_id))
        table.commit()
        cursor.close()
        # logger.info(f'SUCCESS | TEAM WAS UPDATED FOR USER(#{bot_user_class.user_id}).')
        return True
    except sqlite3.Error as error:
        logger.error(f'ERROR | Error with database {error}')
    return False


def create_user(chat, bot_user_class):
    """ CHECK USER IN DB. IF NOT EXIST CREATE NEW USER """

    create_user_table()
    existing_user = check_user_in_db(chat.id)

    if not existing_user:
        try:
            table = sqlite3.connect(db_name)
            cursor = table.cursor()
            cursor.execute(f"INSERT INTO users VALUES(?, ?, ?, ?, ?, ?)",
                           (bot_user_class.user_id, bot_user_class.first_name, bot_user_class.last_name,
                            bot_user_class.username, bot_user_class.email, bot_user_class.team))
            table.commit()
            cursor.close()
            # logger.info('SUCCESS | NEW USER WAS SAVED IN DB.')
        except sqlite3.Error as error:
            logger.error(f'ERROR | Error with database {error}')
    else:
        user = existing_user[0] if existing_user and existing_user[0] else None

        if user:
            bot_user_class.user_id = user[0]
            bot_user_class.first_name = user[1]
            bot_user_class.last_name = user[2]
            bot_user_class.username = user[3]
            bot_user_class.email = user[4]
            bot_user_class.team = user[5]
        # logger.info('SUCCESS | GET INFO ABOUT USER FROM DB.')
    return bot_user_class


def check_user_in_db(user_id):
    """ CHECK USER IN DB """

    try:
        table = sqlite3.connect(db_name)
        cursor = table.cursor()
        cursor.execute(f"SELECT * FROM users WHERE user_id={user_id}")
        response = cursor.fetchall()
        cursor.close()
        # logger.info(f"INFO | Info about user(user_id={user_id}):{response}")
        if response:
            return response
    except sqlite3.Error as error:
        logger.error(f'ERROR | Error with checking user in DB: {error}')
    return False


def create_user_table():
    """ CREATE DB for BOT """

    try:
        table = sqlite3.connect(db_name)
        cursor = table.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(user_id INTEGER, first_name TEXT, last_name TEXT, username TEXT, email TEXT, team TEXT);""")
        table.commit()
        cursor.close()
    except sqlite3.Error as error:
        logger.error(f'ERROR | Error with creating user table: {error}')


def get_all_user_in_db():
    """ GET ALL USERs IN DB """

    try:
        db = sqlite3.connect(db_name)
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM users")
        response = cursor.fetchall()
        cursor.close()
        # logger.info(f"INFO | Info about all users:{response}")
        if response:
            user_id = list()
            for user in response:
                user_id.append(user[0])
            return user_id
    except sqlite3.Error as error:
        logger.error(f'ERROR | Error with checking user in DB: {error}')
    return False


def get_all_user():
    """ GET ALL USERs IN DB """

    try:
        db = sqlite3.connect(db_name)
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM users")
        response = cursor.fetchall()
        cursor.close()
        if response:
            return response
    except sqlite3.Error as error:
        logger.error(f'ERROR | Error with checking user in DB: {error}')
    return False
