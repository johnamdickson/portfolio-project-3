from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import os
from termcolor import colored, cprint
# Testing on Codeanywhere requires local access to api_key on line below
import api_key as api


def get_user_coordinates():
    """
    Prompt user to input latitude and longitude and then perform
    error checking before returning both in a list.
    """
    while True:

        # Taking multiple inputs in one command solution found here:
        # https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/

        colored_note = colored("Note, latitude must be between -90 and 90,"
                               "longitude between -180 and 180.\n",
                               'blue', None, ['bold'])
        try:
            latitude, longitude = input("Please enter your current location's "
                                        "latitude and longitude separated by a"
                                        " whitespace.\n"
                                        + colored_note).split()
        except ValueError as e:
            if e.args[0] == "not enough values to unpack (expected 2, got 1)":
                print(colored("You only made one entry or did not include"
                              " a whitespace, please make two entries - "
                              "one for latitude and another for longitude.",
                              'white', 'on_red', ['bold']))
            elif e.args[0] == "too many values to unpack (expected 2)":
                print(colored("You entered too many numbers, please make two"
                              "entries, one for latitude and another for "
                              "longitude.", 'white', 'on_red', ['bold']))
            continue
        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            print(colored(f"Invalid entry, please enter a number between "
                          "-90 to 90 for latitude and -180 to 180 for "
                          "longitude. ", 'white', 'on_red', ['bold']))
            continue
        else:
            if latitude < -90 or latitude > 90:
                print(colored("Invalid entry, please enter a latitude"
                              " between -90 and 90",
                              'white', 'on_red', ['bold']))
                get_user_coordinates()
                return
            if longitude < -180 or longitude > 180:
                print(colored("Invalid entry, please enter a longitude"
                              " between -180 and 180",
                              'white', 'on_red', ['bold']))
                get_user_coordinates()
                return
            break
    return [latitude, longitude]


def get_user_forecast_selection():
    user_input = 0
    while True:
        try:
            user_input = int(input("How many days would you like forecast?"
                                   "1, 2 or 3 day forecasts available\n"
                                   "Please enter a number from 1 to 3:\n"))
        except ValueError:
            print(colored("Invalid entry, an integer (1,2 or 3) is required.",
                          'white', 'on_red', ['bold']))
            continue
        else:
            if user_input not in range(1, 4):
                print(colored("Invalid number, please enter 1, 2 or 3",
                              'white', 'on_red', ['bold']))          
                get_user_forecast_selection
            elif user_input == 1:
                print("\nLoading weather forecast...")
                get_user_forecast_selection
            break
    return


def get_weather_forecast(coordinates):
    """
    Function to retrieve weather forecast data from coordinates specified
    by user.
    """
    # Maintaining API Key secrecy for deployment to Heroku via environment
    # variable. Solution found in Stack Overflow:
    # https://stackoverflow.com/questions/47949022/git-heroku-how-to-hide-my-secret-key

    # Deploympent to Heroku requires access to environment variable on
    # line below:
    # API_KEY = os.getenv('API_KEY')

    # Testing on Codeanywhere requires local access to api_key on line below
    owm = OWM(api.API_KEY)

    # Use of pyowm library to utilise Open weather API
    # via documentation below:
    # https://pyowm.readthedocs.io/en/latest/

    # Deploympent to Heroku requires access to environment variable on
    # line below
    # owm = OWM(API_KEY)
    latitude = coordinates[0]
    longitude = coordinates[1]
    mgr = owm.weather_manager()
    one_call = mgr.one_call(latitude, longitude)
    print("Getting weather forecast...")
    forecast_weather_dictionary = ([weather.to_dict() for weather
                                    in one_call.forecast_daily])
    # print(forecast_weather_dictionary[0])
    # print(len(forecast_weather_dictionary))

    return forecast_weather_dictionary
