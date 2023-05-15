import gspread
from google.oauth2.service_account import Credentials
import gspread
from google.oauth2.service_account import Credentials
import time
import sys
from termcolor import colored, cprint
import datetime as d
import os
from menus import run_past_weather


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('historical-weather-data')

weather_archive_sheet = SHEET.worksheet('archive')


def find_date_range():
    """
    Calculate date range in worksheet to display to user before making
    their entry.
    """
    earliest_date = weather_archive_sheet.cell(2, 1).value
    row_count = len(weather_archive_sheet.get_all_values())
    latest_date = weather_archive_sheet.cell(row_count, 1).value
    return [earliest_date, latest_date]


def find_historical_data_row(date, date_range):
    """
    Function to find row in historical data spreadsheet and return data from
    row as list.
    """
    # Solution to selecting cell from Stack Overflow:
    # https://stackoverflow.com/questions/65234180/how-to-find-a-row-based-on-an-id-and-then-edit-the-row-with-gspread-python
    print(f"Locating data for {date}...")
    try:
        # look for cell in spreadsheet that matches the date entered 
        # and return row data for the cell's row.
        cell = weather_archive_sheet.find(date, in_column=1)
        weather_data = weather_archive_sheet.row_values(cell.row)
        print(weather_data)
        return weather_data
    except AttributeError:
        # Handle error by informing user of exception and then re-running the main() function.
        os.system('clear')
        print(colored(f"The date you selected is not available. You entered '{date}'\n\nDate should be between {date_range[0]} and {date_range[1]}.\n",
                    'white', 'on_red',['bold']))
        run_past_weather()


def get_date(sheet_dates):
    """
    Request date from user to locate historical weather data.
    """
    os.system('clear')
    while True:
        # Solution to highlighting text found in stack overflow:
        # https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python
        earliest_date = colored(sheet_dates[0], 'green', 'on_black',
                                ['bold'])
        latest_date = colored(sheet_dates[1], 'green', 'on_black',
                                ['bold'])
        print(f"Please enter the date to check the historical weather data for Dublin Airport.\n")
        time.sleep(1.5)
        print(f"Available dates between {earliest_date} and {latest_date}.\n")
        time.sleep(1)
        print("The date format should be: DD/MM/YYYY e.g 30/04/1978\n")
        time.sleep(1)
        date = input("Enter your date below:\n")
        if validate_date(date):
            # Give user feedback the data is valid and then break from
            # While loop to return date.
            os.system('clear')
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
    date_format = '%d/%m/%Y'

    # using try-except blocks for handling the exceptions
    try:
        # formatting the date using strptime() function
        d.datetime.strptime(date, date_format)
        return True

    # If the date validation goes wrong
    except ValueError:
        # printing the appropriate text if ValueError occurs
        os.system('clear')
        print(colored(f"""Incorrect data format, you entered '{date}'\nDate should be in the format DD/MM/YYYY e.g. 30/04/1978\n""",
                    'white', 'on_red',['bold']))
        time.sleep(4)
        os.system('clear')
        return False
    else:
        return True