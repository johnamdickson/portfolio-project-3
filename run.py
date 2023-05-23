import past_weather as past
from classes import PastWeather, ForecastWeather
import time
from termcolor import colored, cprint
import os
import menus
import weather_forecast as wf


def main():
    # menus.main_menu()
    coordinates = wf.get_user_coordinates()
    get_forecast = wf.get_weather_forecast(coordinates)
    forecast = ForecastWeather(get_forecast)
    forecast.parse_forecast()

main()