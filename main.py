import past_weather as past
from classes import PastWeather, Feedback, ForecastWeather, LoadingScreens
import time
from termcolor import colored, cprint
import os
import weather_forecast as wf
import weather_constants as constants
import threading


def user_options():
    """
    Function to assign 4 options to user on completion
    of past weather or forecast weather code.
    """
    user_input = 0
    while True:
        try:
            user_input = int(input("\nPress 1 to return to Main Menu\n"
                                   "Press 2 to look for past weather"
                                   "\nPress 3 for forecast at your "
                                   "chosen location\n"
                                   "Press 4 to leave feedback\n"))
        except ValueError:
            print(colored("Invalid entry, please enter an integer"
                          " between 1 and 4\n", 'white', 'on_red',
                          ['bold']))
            continue
        else:
            if user_input not in range(1, 5):
                print(colored("Invalid entry, please enter an integer"
                              " between 1 and 4\n", 'white', 'on_red',
                              ['bold']))
            break
    return user_input


def restart_user_selection(choice):
    """
    Using selection passed in from PastWeather class instance,
    select appropriate menu.
    """
    if choice == 1:
        os.system('clear')
        main_menu()
    elif choice == 2:
        os.system('clear')
        run_past_weather()
    elif choice == 3:
        os.system('clear')
        run_weather_forecast()
    elif choice == 4:
        os.system('clear')
        print("Loading feedback...")
        run_feedback()
    return


def run_feedback():
    feedback = Feedback()
    feedback.get_feedback()
    main_menu()


def run_past_weather():
    """
    Function to run past weather main functions and 
    instantiate respective class.
    """
    # Use of threading and loading screens class to create animation
    # whilst call is being made to Google sheets. Solution found here:
    # https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-running
    loading = LoadingScreens(False, constants.LOADING_CONSTANT)
    t = threading.Thread(target=loading.animate)
    t.start()
    # perform check of Google sheet.
    available_dates = past.find_date_range()
    # loading completion by passing in true to 'loading' instance.
    loading.complete = True
    # sleep for one second to prevent clearing screen during past weather 
    # terminal information printed for user.
    time.sleep(0.5)
    user_date = past.get_date(available_dates)
    loading.complete = False
    t_2 = threading.Thread(target=loading.animate)
    t_2.start()
    historical_data = past.find_historical_data_row(user_date, available_dates)
    loading.complete = True
    if historical_data[0] != True:
        loading.complete = True
        os.system('clear')
        time.sleep(0.5)
        print(historical_data[1])
        time.sleep(4)
        run_past_weather()
    else:
        past_weather = PastWeather(historical_data[1], user_date)
        loading_complete = True
        # sleep for one second to prevent clearing screen during past weather 
        # terminal information printed for user.
        time.sleep(1)
        past_weather.parse_data()
        user_option = user_options()
        restart_user_selection(user_option)


def run_weather_forecast():
    """
    Function to run weather forecast main functions and 
    instantiate respective class.
    """
    os.system('clear')
    coordinates = wf.get_user_coordinates()
    loading = LoadingScreens(False, constants.LOADING_CONSTANT)
    t = threading.Thread(target=loading.animate)
    t.start()
    # get data from Open Weather API
    get_forecast = wf.get_weather_forecast(coordinates)
    # loading completion by passing in true to 'loading' instance.
    loading.complete = True
    # Sleep for one second to prevent clearing screen during forecast
    # weather terminal information printed for user.
    time.sleep(1)
    # Check if get_forecast call was successful, based on boolean
    # passed from function return.
    if get_forecast[0] == False:
        cprint("Sorry, the following error was encountered:\n"
               f" ** {get_forecast[1][0]} ** ", 'white', 'on_red', ['bold'])
        print("\nPlease select an option:")
        user_option = user_options()
        restart_user_selection(user_option)
    else:
        forecast = ForecastWeather(get_forecast[1])
        # Create parsed three day forecast dictionaries by calling parse_forecast
        # method.
        forecast.parse_forecast()
        # Create forecast from three day dictionaries and then print each to 
        # console followed by user prompts to move to next or menu options at end.
        day_one = forecast.create_forecast(forecast.day_one_parsed)
        forecast.print_forecast_to_console(1, day_one)
        forecast.move_to_next_day()
        day_two = forecast.create_forecast(forecast.day_two_parsed)
        forecast.print_forecast_to_console(2, day_two)
        forecast.move_to_next_day()
        day_three = forecast.create_forecast(forecast.day_three_parsed)
        forecast.print_forecast_to_console(3, day_three)
        user_option = user_options()
        restart_user_selection(user_option)


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
    # Instantiate loading screen class for title and then 
    # call animate method followed by a delay before 
    # updating complete status to true to move on through
    # program.
    loading = LoadingScreens(False, constants.TITLE_CONSTANT)
    loading.animate()
    time.sleep(2)
    loading.complete = True
    os.system('clear')
    print("Welcome to Weather: Past or Forecast?\n"
          "\nThe app which lets you review historical"
          " weather at Dublin Airport or access a"
          " 3 day weather forecast for your location.\n"
          "\nPress 1 for past weather.\nPress 2 for "
          "the weather forecast.\n")
    user_selection()
