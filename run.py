import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('historical-weather-data')

worksheet_test = SHEET.worksheet('archive')
# print(worksheet_test.row_values(1))

def find_historical_data_row(date):
    """
    Function to find row in historical data spreadsheet and return data from row as list.
    """
    # Solution to selecting cell from Stack Overflow:
    # https://stackoverflow.com/questions/65234180/how-to-find-a-row-based-on-an-id-and-then-edit-the-row-with-gspread-python
    cell = worksheet_test.find(date,in_column = 1)
    weather_data = worksheet_test.row_values(cell.row)
    print (weather_data)
    return weather_data

find_historical_data_row('01/01/1942')