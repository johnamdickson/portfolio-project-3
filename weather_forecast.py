from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import os
from termcolor import colored, cprint
import main
from os import system
from time import sleep
import functions as f

# Testing on Codeanywhere requires local access to api_key on line below
# import api_key as api


def get_user_coordinates():
    """
    Prompt user to input latitude and longitude and then perform
    error checking before returning both in a list.
    """
    while True:
        
        # Taking multiple inputs in one command solution found here:
        # https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/

        colored_latitude = colored("-90 and 90,",'green', None, ['bold'])
        colored_longitude = colored("-180 and 180.", 'green', None, ['bold'])
        print("Please enter your chosen location's latitude and longitude "
              "separated by a\nwhitespace.\n")
        print(f"Note, latitude must be between {colored_latitude} longitude"
              f" between {colored_longitude}\n")
        print("Latitudes west of the Prime Meridian(Greenwich, London) and "
              "longitudes south of the equator should be negative.\n")
        try:
            latitude, longitude = input(f"Please enter coordinates below:\n").split()
        except ValueError as e:
            if e.args[0] == "not enough values to unpack (expected 2, got 1)":
                f.print_error_message("You only made one entry or did not include"
                                      " a whitespace, please make two entries - "
                                      "one for latitude and another for longitude.", 3)
            elif e.args[0] == "too many values to unpack (expected 2)":
                f.print_error_message("You entered too many numbers, please make two"
                                      " entries, one for latitude and another for "
                                      "longitude.", 3)
            continue
        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            f.print_error_message("Invalid entry, please enter a number between "
                                  "-90 to 90 for latitude and -180 to 180 for "
                                  "longitude. ", 3)
            continue
        else:
            if latitude < -90 or latitude > 90:
                f.print_error_message("Invalid entry, please enter a latitude"
                                      " between -90 and 90", 3)
                continue
            elif longitude < -180 or longitude > 180:
                f.print_error_message("Invalid entry, please enter a longitude"
                                      " between -180 and 180", 3)
                continue
            break
    return [latitude, longitude]


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
    API_KEY = os.getenv('API_KEY')

    # Testing on Codeanywhere requires local access to api_key on line below
    # owm = OWM(api.API_KEY)

    # Use of pyowm library to utilise Open weather API
    # via documentation below:
    # https://pyowm.readthedocs.io/en/latest/

    # Deploympent to Heroku requires access to environment variable on
    # line below
    owm = OWM(API_KEY)
    latitude = coordinates[0]
    longitude = coordinates[1]
    # instantiate weather manager
    mgr = owm.weather_manager()

    # insantiate geocoding manager.
    geo_mgr = owm.geocoding_manager()
    # obtain forecast and location from Open Weather using coordinates.
    try:
        one_call = mgr.one_call(latitude, longitude)
        forecast_weather_dictionary = ([weather.to_dict() for weather
                                    in one_call.forecast_daily])
        location = geo_mgr.reverse_geocode(latitude, longitude)
        location_dict = [location.to_dict() for location in location]
    # Following code to handle any errors coming back from OWM API
    # Tutorial below used for Exceptions:
    # https://docs.python.org/3/tutorial/errors.html
    except Exception as err:
        return False, err.args
    else:
        return True, forecast_weather_dictionary, location_dict



 