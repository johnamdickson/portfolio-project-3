import gspread
from google.oauth2.service_account import Credentials
import time
import sys
from termcolor import colored, cprint
import datetime as d
import os

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('historical-weather-data')

FEEDBACK_SHEET = SHEET.worksheet('feedback')


def get_feedback():
    """
    Request user inputs for name and feeback, perform confirmation step and 
    upload to spreadsheet.
    """
    os.system('clear')
    name_input = input('Please enter your name or leave blank to remain anonymous:\n')
    if name_input == "":
        name_input = "anonymous"
    feedback_input = input('Please enter your feedback:\n')
    now = d.datetime.now()
    date_input = now.strftime("%d/%m/%Y, %H:%M:%S")
    feedback_data = [name_input, feedback_input, date_input]
    print(f"Updloading feedback...\n")
    FEEDBACK_SHEET.append_row(feedback_data)
    print(f"Feedback uploaded, thank you.\n")