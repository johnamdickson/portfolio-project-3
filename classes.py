import datetime as d
import time
import os

class PastWeather:
    """
    Class for past weather data and methods
    """
    def __init__(self, weather_data, date):
        self.weather_data = weather_data
        self.date = date

    def parse_data(self):
        """
        Select pertinent information from Dublin Airport historical weather data
        spreadsheet and return a string detailing all info.
        """
        data = self.weather_data
        max_temp = data[2]
        min_temp = data[4]
        rain = data[8]
        atmos_pressure = data[9]
        mean_wind_speed = data[10]
        sunshine_duration = data[17]
        sunshine_string = ["were", "hours"]
        # Code below to calculate day of the week from date using datetime strftime method.
        # Used following tutorial: https://www.programiz.com/python-programming/datetime/strftime
        date_format = '%d/%m/%Y'
        date = d.datetime.strptime(self.date, date_format)
        day = date.strftime('%A')
        # Code below to handle singular sunshine hour with correct grammar returned in 
        # instance of 1 hour of sunshine.
        if int(sunshine_duration) == 1:
            sunshine_string = ["was", "hour"]

        os.system('clear')

        print(f"{self.date} was a Sunday.")
        time.sleep(2)
        print(f"On that day at Dublin Airport the maximum temperature was {max_temp}°C and the minimum temperature was {min_temp}°C.")
        time.sleep(3)
        print(f"There {sunshine_string[0]} {sunshine_duration} {sunshine_string[1]} of sunshine with a total rainfall of {rain} mm.")
        time.sleep(3)
        print(f"The mean wind speed for the day was {mean_wind_speed} knots with an atmospheric pressure of {atmos_pressure} mbar.")
