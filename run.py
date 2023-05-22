import past_weather as past
from classes import PastWeather, ForecastWeather
import time
from termcolor import colored, cprint
import os
import menus
import weather_forecast as wf


def main():
    # menus.main_menu()
    wf.get_user_coordinates()
    # get_forecast = wf.get_weather_forecast(53.90026, -9.60260)
    # forecast = ForecastWeather(get_forecast)
    # forecast.parse_forecast()

main()