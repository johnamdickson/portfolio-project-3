import gspread
from google.oauth2.service_account import Credentials
import time
import sys
import datetime

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
    Function to find row in historical data spreadsheet and return data from 
    row as list.
    """
    # Solution to selecting cell from Stack Overflow:
    # https://stackoverflow.com/questions/65234180/how-to-find-a-row-based-on-an-id-and-then-edit-the-row-with-gspread-python
    print(f"Locating data for {date}")
    cell = worksheet_test.find(date, in_column=1)
    weather_data = worksheet_test.row_values(cell.row)
    print(weather_data)
    return weather_data

def get_date():
    """
    Request date from user to locate historical weather data.
    """
    while True:
        print("Please enter the date to check the historical weather data.")
        print("The date format should be: DD/MM/YYYY")
        print("Example: 30/04/1978\n")
        date = input("Enter your date here:\n")
        if validate_date(date):
            print("Date is valid!")
            break
    return date

def validate_date(date):
    """Inside the try, creates a date object using datetiem class strptime 
    method. Raises ValueError if date does not conform to date format.
    """
    # The following tutorial was used to determine the correct date format.
    # https://www.tutorialspoint.com/How-to-do-date-validation-in-Python

    # giving the date format
    date_format = '%d/%M/%Y'

    # using try-except blocks for handling the exceptions
    try:
        # formatting the date using strptime() function
        dateObject = datetime.datetime.strptime(date, date_format)
        return True
    # If the date validation goes wrong
    except ValueError:
        # printing the appropriate text if ValueError occurs
        print("Incorrect data format, should be DD/MM/YYYY\n")
        return False

def main():
    user_date = get_date()
    find_historical_data_row(user_date)

main()