import past_weather as past
from classes import PastWeather, Feedback, ForecastWeather
import time
from termcolor import colored, cprint
import os
import weather_forecast as wf
import weather_icons as icons


def loading_screens(icons):
    """
    Helper function to manage screen loading for
    3 options taking in parameter of loading screen
    type to calculate required loading screen option.
    """
    os.system('clear')
    cprint(f"{icons[0]} end='\r'", 'red', 'on_white', ['bold'])
    time.sleep(1)
    os.system('clear')
    cprint(f"{icons[1]} end='\r'", 'red', 'on_white', ['bold'])
    time.sleep(1)
    os.system('clear')
    cprint(f"{icons[2]} end='\r'", 'red', 'on_white', ['bold'])
    os.system('clear')
    return


def run_feedback():
    feedback = Feedback()
    feedback.get_feedback()
    main_menu()


def restart_user_selection(choice):
    """
    Using selection passed in from PastWeather class instance,
    select appropriate menu.
    """
    if choice == 1:
        print("Returning to main menu...")
        main_menu()
    elif choice == 2:
        os.system('clear')
        print("Loading past weather...☼")
        run_past_weather()
    elif choice == 3:
        os.system('clear')
        print("Loading weather forecast...")
        run_weather_forecast()
    elif choice == 4:
        os.system('clear')
        print("Loading feedback...")
        run_feedback()
    return
 

def run_past_weather():
    """
    Function to run past weather main functions and 
    instantiate respective class.
    """
    available_dates = past.find_date_range()
    user_date = past.get_date(available_dates)
    historical_data = past.find_historical_data_row(user_date, available_dates)
    past_weather = PastWeather(historical_data, user_date)
    past_weather.parse_data()
    user_option = past_weather.user_options()
    restart_user_selection(user_option)


def run_weather_forecast():
    """
    Function to run weather forecast main functions and 
    instantiate respective class.
    """
    coordinates = wf.get_user_coordinates()
    get_forecast = wf.get_weather_forecast(coordinates)
    forecast = ForecastWeather(get_forecast)
    forecast.parse_forecast()


def user_selection():
    user_input = 0
    while True:
        try:
            user_input = int(input("Please make a selection:"))
        except ValueError:
            print(colored("Invalid entry, an integer (1 or 2) is required.",
                          'white', 'on_red', ['bold']))
            continue
        else:
            if user_input not in range(1, 3):
                cprint("Invalid number, please enter 1 or 2",
                       'white', 'on_red', ['bold'])         
                user_selection()
            elif user_input == 1:
                loading_screens(icons.PAST_WEATHER_LOADING)
                run_past_weather()
            else:
                os.system('clear')

                run_weather_forecast()
            break
    return


def main_menu():
    os.system('clear')
    print("Welcome to Weather: Past or Forecast?\n")
    time.sleep(2)
    print("Press 1 for past weather.\nPress 2 for the weather forecast.\n")
    user_selection()