import past_weather as past
from classes import PastWeather, Feedback, ForecastWeather, LoadingScreens
from time import sleep
from termcolor import colored, cprint
from os import system
import weather_forecast as wf
import constants as const
import threading
import functions as f

def user_options(number_of_options):
    """
    Function to assign 4 options to user on completion
    of past weather or forecast weather code.
    """
    while True:
        user_input = 0
        five_options = ("\nPress 1 to return to main menu\nPress 2 "
                    "to look for past weather \nPress 3 for forecast"
                    " at your chosen location\nPress 4 to leave" 
                    "feedback\nPress 5 to see the 3 day summary.\n")
        four_options = ("\nPress 1 to return to main menu\nPress 2 "
                    "to look for past weather \nPress 3 for forecast"
                    " at your chosen location\nPress 4 to leave "
                    "feedback.\n")
        try:
            if number_of_options == 5:
                user_input = int(input(five_options))
            else:
                user_input = int(input(four_options))
        except ValueError:
            if number_of_options == 5:
                f.print_error_message("Invalid entry, please enter an integer"
                                      " between 1 and 5", 3)
                continue
            else:
                f.print_error_message("Invalid entry, please enter an integer"
                                      " between 1 and 4", 3)
                continue
        else:
            if number_of_options == 5:
                if user_input not in range(1, 6):
                    f.print_error_message("Invalid entry, please enter an integer"
                                  " between 1 and 5", 3)
                    continue
                else:
                    break
            elif number_of_options == 4:
                if user_input not in range(1, 5):
                    f.print_error_message("Invalid entry, please enter an integer"
                                          " between 1 and 4", 3)
                    continue
                else:
                    break
    return user_input


def restart_user_selection(choice):
    """
    Using selection passed in from PastWeather class instance,
    select appropriate menu.
    """
    if choice == 1:
        system('clear')
        main_menu()
    elif choice == 2:
        system('clear')
        run_past_weather()
    elif choice == 3:
        system('clear')
        run_weather_forecast()
    elif choice == 4:
        system('clear')
        print("Loading feedback...")
        run_feedback()
    return


def run_feedback():
    """
    Function to create instance of Feedback class
    and call methods in the correct order.
    """
    feedback = Feedback()
    feedback.create_feedback()
    feedback.read_feedback()
    main_menu()


def run_past_weather():
    """
    Function to run past weather main functions and 
    instantiate respective class.
    """
    # Use of threading and loading screens class to create animation
    # whilst call is being made to Google sheets. Solution found here:
    # https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-running
    loading = LoadingScreens(False, const.LOADING_CONSTANT)
    thread = threading.Thread(target=loading.animate)
    thread.start()
    # perform check of Google sheet.
    available_dates = past.find_date_range()
    # loading completion by passing in true to 'loading' instance.
    loading.complete = True
    # sleep for one second to prevent clearing screen during past weather 
    # terminal information printed for user.
    sleep(0.5)
    user_date = past.get_date(available_dates)
    loading.complete = False
    thread_2 = threading.Thread(target=loading.animate)
    thread_2.start()
    historical_data = past.find_historical_data_row(user_date, available_dates)
    loading.complete = True
    if historical_data[0] != True:
        loading.complete = True
        sleep(0.5)
        f.print_error_message(historical_data[1], 4)
        run_past_weather()
    else:
        past_weather = PastWeather(historical_data[1], user_date)
        loading_complete = True
        # sleep for one second to prevent clearing screen during past weather 
        # terminal information printed for user.
        sleep(1)
        weather_data = past_weather.parse_data()
        past_weather.print_weather_to_console(weather_data)
        user_option = user_options(4)
        restart_user_selection(user_option)


def run_weather_forecast():
    """
    Function to run weather forecast main functions and 
    instantiate respective class.
    """
    system('clear')
    coordinates = wf.get_user_coordinates()
    loading = LoadingScreens(False, const.LOADING_CONSTANT)
    thread = threading.Thread(target=loading.animate)
    thread.start()
    # get data from Open Weather API
    get_forecast = wf.get_weather_forecast(coordinates)
    # loading completion by passing in true to 'loading' instance.
    loading.complete = True
    # Sleep for one second to prevent clearing screen during forecast
    # weather terminal information printed for user.
    sleep(1)
    # Check if get_forecast call was successful, based on boolean
    # passed from function return.
    if get_forecast[0] == False:
        f.print_error_message("Sorry, the following error was encountered:\n"
                              f" ** {get_forecast[1][0]} ** ", 3)
        print("\nPlease select an option:")
        user_option = user_options(4)
        restart_user_selection(user_option)
    else:
        forecast = ForecastWeather(get_forecast[1], get_forecast[2])
        # Create parsed three day forecast dictionaries by calling parse_forecast
        # method.
        forecast.parse_forecast()
        # Create forecast from three day dictionaries and then print each to 
        # console followed by user prompts to move to next or menu options at end.
        day_one = forecast.create_forecast(forecast.day_one_parsed)
        forecast.print_forecast_to_console(1, day_one, coordinates)
        forecast.move_to_next_day()
        day_two = forecast.create_forecast(forecast.day_two_parsed)
        forecast.print_forecast_to_console(2, day_two, coordinates)
        forecast.move_to_next_day()
        day_three = forecast.create_forecast(forecast.day_three_parsed)
        forecast.print_forecast_to_console(3, day_three, coordinates)
        user_option = user_options(5)
        if user_option == 5:
            forecast.print_three_day_summary(day_one, day_two, day_three)
            input("Hit return to access other user options.")
            user_option = user_options(4)
            restart_user_selection(user_option)
        else:
            restart_user_selection(user_option)


def user_selection():
    """
    Main menu selection for user at initiation of the 
    app.
    """
    user_input = 0
    while True:
        print("Welcome to Weather: Past or Forecast?\n"
              "\nThe app which lets you review historical"
              " weather at Dublin Airport or access a\n"
              " 3 day weather forecast for your location.\n"
              "\nPress 1 for past weather.\nPress 2 for "
              "the weather forecast.\n")
        try:
            user_input = int(input("Please make a selection:"))
        except ValueError:
            f.print_error_message("Invalid entry, an integer (1 or 2) is required.", 3)
            continue
        else:
            if user_input not in range(1, 3):
                f.print_error_message("Invalid number, please enter 1 or 2", 3)
                continue
            elif user_input == 1:
                system('clear')
                run_past_weather()
            else:
                system('clear')
                run_weather_forecast()
            break
    return


def main_menu():
    system('clear')
    # Instantiate loading screen class for title and then 
    # call animate method followed by a delay before 
    # updating complete status to true to move on through
    # program.
    loading = LoadingScreens(False, const.TITLE_CONSTANT)
    loading.animate()
    sleep(2)
    loading.complete = True
    system('clear')
    user_selection()

