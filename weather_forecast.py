from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import os
import api_key as api


def get_weather_forecast(latitude, longitude):
    """
    Function to retrieve weather forecast data from coordinates specified
    by user.
    """
    # Maintaining API Key secrecy for deployment to Heroku via environment 
    # variable. Solution found in Stack Overflow:
    # https://stackoverflow.com/questions/47949022/git-heroku-how-to-hide-my-secret-key
    # API_KEY = os.getenv('API_KEY')
    owm = OWM(api.API_KEY)

    # Use of pyowm library to utilise Open weather API
    #  via documentation below:
    # https://pyowm.readthedocs.io/en/latest/

    # owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    one_call = mgr.one_call(latitude, longitude)
    print("Getting weather forecast...")
    forecast_weather_dictionary = [weather.to_dict() for weather in one_call.forecast_daily]
    print(forecast_weather_dictionary[0])
    print(len(forecast_weather_dictionary))

    return forecast_weather_dictionary