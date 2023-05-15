import past_weather as past
from classes import PastWeather
import time
from termcolor import colored, cprint
import os
import menus


# def run_past_weather():
#     """
#     Contains all necessary functions to run the past 
#     weather part of app.
#     """
#     available_dates = past.find_date_range()
#     user_date = past.get_date(available_dates)
#     historical_data = past.find_historical_data_row(user_date, available_dates)
#     class_test = PastWeather(historical_data, user_date)
#     class_test.parse_data()


# def user_selection():
#     user_input = 0
#     while True:
#         try:
#             user_input = int(input("Please make a selection:"))
#         except ValueError:
#             print(colored(f"Invalid entry, an integer (1 or 2) is required.",
#                 'white', 'on_red', ['bold']))
#             continue
#         else:
#             if user_input not in range(1, 3):
#                 print(colored(f"Invalid entry, please enter 1 or 2",
#                     'white', 'on_red',['bold']))          
#                 user_selection()
#             elif user_input == 1:
#                 print("\nLoading past weather...")
#                 run_past_weather()
#             else:
#                 print("Selected forecast.")
#             break
#     return


def main():
    menus.main_menu()
    # os.system('clear')
    # print("Welcome to Weather: Past or Forecast?\n")
    # time.sleep(2)
    # print("Press 1 for past weather.\nPress 2 for the weather forecast.\n")
    # time.sleep(1)
    # user_selection()


main()