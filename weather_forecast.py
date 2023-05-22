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
    error checking before returning as a list.
    """
    while True:
        # Taking multiple inputs in one command solution found here:
        #https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
        try: latitude, longitude = input("""
Please enter your current location's latitude and longitude separated by a 
whitespace. Remember, latitude is between -90 and 90, longitude between -180 and 180.
        """).split()
        except ValueError as e:
            if e.args[0] == "not enough values to unpack (expected 2, got 1)":
                print(colored(f"""
You only entered one number or did not include a whitespace, please make two 
entries - one for latitude and another for longitude.""",
                'white', 'on_red', ['bold']))
            elif e.args[0] == "too many values to unpack (expected 2)":
                print(colored(f"""
You entered too many numbers, please make two entries, one for latitude
and another for longitude.""",
                'white', 'on_red', ['bold']))
            continue
        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError as e:
            print(e)
            print(colored(f"Invalid entry, please enter a number between -90 to 90 for latitude and -180 to 180 for longitude. ",
                'white', 'on_red', ['bold']))
            continue
        else:
            if latitude < -90 or latitude > 90:
                print(colored(f"Invalid entry, please enter a latitude between -90 and 90",
                    'white', 'on_red',['bold']))
                get_user_coordinates()
                return

            if longitude < -180 or longitude > 180:
                print(colored(f"Invalid entry, please enter a longitude between -180 and 180",
                    'white', 'on_red',['bold']))
                get_user_coordinates()
                return
            break
    print(f"Made it through, here is the lat {latitude} and lon {longitude}")
    return [latitude, longitude]

def get_weather_forecast(latitude, longitude):
    """
    Function to retrieve weather forecast data from coordinates specified
    by user.
    """
    # Maintaining API Key secrecy for deployment to Heroku via environment 
    # variable. Solution found in Stack Overflow:
    # https://stackoverflow.com/questions/47949022/git-heroku-how-to-hide-my-secret-key

    #Deploympent to Heroku requires access to environment variable on line below:
    # API_KEY = os.getenv('API_KEY')

    # Testing on Codeanywhere requires local access to api_key on line below
    owm = OWM(api.API_KEY)

    # Use of pyowm library to utilise Open weather API
    #  via documentation below:
    # https://pyowm.readthedocs.io/en/latest/

    #Deploympent to Heroku requires access to environment variable on line below
    # owm = OWM(API_KEY)
    
    mgr = owm.weather_manager()
    one_call = mgr.one_call(latitude, longitude)
    print("Getting weather forecast...")
    forecast_weather_dictionary = [weather.to_dict() for weather in one_call.forecast_daily]
    # print(forecast_weather_dictionary[0])
    # print(len(forecast_weather_dictionary))

    return forecast_weather_dictionary