## PHD&Bigbro.ai

#### Created by Ivan Gavrilov

------
#### **Описание задачи:**
***Данный Telegram-бот предназначен для регистрации и сбора контактных данных участников турнира по футболу для дальнейшей рассылки видео и результатов***
_________
### _Требования_ 
Для корректной работы бота требуется Python версии не ниже 3.8, а также следующие модули:

```
apiclient==1.0.4  
cachetools==5.3.3  
certifi==2024.2.2  
charset-normalizer==3.3.2  
colorama==0.4.6  
google-api-core==2.19.0  
google-api-python-client==2.130.0  
google-auth==2.29.0  
google-auth-httplib2==0.2.0  
google-auth-oauthlib==1.2.0  
googleapis-common-protos==1.63.0  
httplib2==0.22.0  
idna==3.7  
loguru==0.7.2  
oauth2client==4.1.3  
oauthlib==3.2.2  
proto-plus==1.23.0  
protobuf==4.25.3  
pyasn1==0.6.0  
pyasn1_modules==0.4.0  
pyparsing==3.1.2  
pyTelegramBotAPI==4.17.0  
python-decouple==3.6  
requests==2.31.0  
requests-oauthlib==2.0.0  
rsa==4.9  
six==1.16.0  
uritemplate==4.1.1  
urllib3==2.2.1  
win32-setctime==1.1.0
```
---
### _Файловый состав бота_
Бот использует технологию polling, поэтому дополнительного конфигурирования сервера не требуется.
В составе бота используются следующие файлы:
* main.py - основной файл работы телеграм-бота
* messages.py - файл, содержащий функции для вывода различных сообщений
* sheet_actions.py - файл, содержащий функции для записи данных в Google Sheets
* db_funcs.py - файл, содержащий функции для CRUD концепции работы с БД SQLite3
* .env - файл, содержащий токен подключения бота к серверам Telegram и токен подключения к API hotels.com. Этот файл необходимо создать вручную
* requirements.txt - список необходимых модулей
* class_user.py - файл, содержащий класс пользователя для его инициализации 
---
### _Подготовка к запуску_
Для функционирования бота вам сначала необходимо зарегистрировать бота в Telegram с помощью @BotFather.
Полученные токены необходимо расположить в файле ".env":
* phd_bot = 'токен, полученный от @BotFather в Telegram'
* credentials_file = 'JSON ключ к доступу к файлу'
* spreadsheet_id = 'ключ, полученный от Google Sheets к используемому файлу'
---
### _Запуск_

1. Создание виртуальной среды:
``` 
python -m venv venv
```

2. Установка зависимостей проекта:
```
pip install -r requirements.txt
```

3. Активация виртуальной среды:
```
cd venv\Scripts\activate
```

4.  Запуск бота:
```
python main.py
```
---
### После запуска бот начнёт функционировать в Telegram под именем [PHD_Bigbro_bot](https://t.me/PHD_Bigbro_bot)
---
### _Список команд для взаимодействия с ботом:_ 
* /start - Приветствие с пользователем
* /help - Вывод списка команд для бота
* /email - Изменить электронную почту пользователя
* /team - Изменить команду пользователя
