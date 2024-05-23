from oauth2client.service_account import ServiceAccountCredentials
from decouple import config
import apiclient.discovery
import httplib2


CREDENTIALS_FILE = config('credentials_file') # Имя файла с закрытым ключом
spreadsheet_id = config('spreadsheet_id') # ID Google Sheets документа (можно взять из его URL)

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
)
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)


def insert_values(info):
    """ Add INFO in google sheets """

    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        valueInputOption="USER_ENTERED",
        range="Users!A1",
        body={
            "values": [info]
        }
    ).execute()
