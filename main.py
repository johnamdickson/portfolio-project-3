import past_weather as past
from classes import PastWeather, Feedback, ForecastWeather, LoadingScreens
import time
from termcolor import colored, cprint
import os
import weather_forecast as wf
import weather_constants as constants
import threading

    

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
    # Use of threading and loading screens class to create animation
    # whilst call is being made to Google sheets. Solution found here:
    # https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-running
    loading = LoadingScreens(False, "Past Weather ")
    t = threading.Thread(target=loading.animate)
    t.start()
    # perform check of Google sheet.
    available_dates = past.find_date_range()
    # loading completion by passing in true to 'loading' instance.
    loading.complete = True
    # sleep for one second to prevent clearing screen during past weather 
    # terminal information printed for user.
    time.sleep(1)
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
    """
    Main menu selection for user at initiation of the 
    app.
    """
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