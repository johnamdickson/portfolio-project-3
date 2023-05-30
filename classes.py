import datetime as d
import time
import os
from termcolor import colored, cprint
import gspread
from google.oauth2.service_account import Credentials
import numpy as np
import constants as const
import itertools


class PastWeather:
    """
    Class for past weather data and associated methods
    """

    def __init__(self, weather_data, date):
        self.weather_data = weather_data
        self.date = date

    def parse_data(self):
        """
        Select pertinent information from Dublin Airport historical weather
        data spreadsheet and return a string detailing all info.
        """
        data = self.weather_data
        max_temp = colored(data[2] + "°C", 'blue', None, ['bold'])
        min_temp = colored(data[4] + "°C", 'blue', None, ['bold'])
        rain = colored(data[8] + " mm", 'blue', None, ['bold'])
        atmos_pressure = colored(data[9] + " mbar", 'blue', None, ['bold'])
        mean_wind_speed = colored(data[10] + " knots", 'blue', None, ['bold'])
        sunshine_duration = data[17]
        sunshine_duration_string = colored(data[17], 'blue', None, ['bold'])
        sunshine_string = ["were", "hours"]
        # Code below to calculate day of the week from date using
        # datetime strftime method. Used following tutorial:
        # https://www.programiz.com/python-programming/datetime/strftime
        date_format = '%d/%m/%Y'
        date = d.datetime.strptime(self.date, date_format)
        day = date.strftime('%A')
        # Code below to handle singular sunshine hour with correct grammar
        # returned in instance of 1 hour of sunshine.
        if float(sunshine_duration) == 1:
            sunshine_string = ["was", "hour"]
        # Clear terminal and print out readable data to user with
        # pauses in between for effect.
        os.system('clear')
        print(f"{self.date} was a {colored(day, 'blue', None, ['bold'])}.")
        time.sleep(2)
        print("On that day at Dublin Airport the maximum temperature was "
              f"{max_temp} and the minimum temperature was {min_temp}."
              )
        time.sleep(3)
        print(f"There {sunshine_string[0]} {sunshine_duration_string} "
              f"{colored(sunshine_string[1], 'blue', None, ['bold'])} "
              f"of sunshine with a total rainfall of {rain}")
        time.sleep(3)
        print(f"The mean wind speed for the day was {mean_wind_speed}"
              f" with an atmospheric pressure of {atmos_pressure}.")
        time.sleep(2)


class Feedback:
    """
    Class for user feedback on past weather with associated methods
    """
    SCOPE = [
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive.file",
                "https://www.googleapis.com/auth/drive"
                ]

    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open('historical-weather-data')
    # Access spreadsheet feedback sheet.
    FEEDBACK_SHEET = SHEET.worksheet('feedback')

    def __init__(self):
        return
    
    def delete_feedback(self, row_count):
        self.FEEDBACK_SHEET.delete_rows(row_count)
        return
        
    def update_feedback(self, column, row):
        if column == 1:
            name = input("Please update your name:")
            self.FEEDBACK_SHEET.update_cell(row, column, name)
            self.read_feedback()
        if column == 2:
            feedback = input("Please update your feedback:")
            self.FEEDBACK_SHEET.update_cell(row, column, feedback)
            self.read_feedback()

    def read_feedback(self):
        """
        function to elicit response from user to ensure name and
        feedback are correct with checks to confirm correct inputs
        with associated user feedback.
        """
        row_count = len(self.FEEDBACK_SHEET.get_all_values())
        feedback = self.FEEDBACK_SHEET.row_values(row_count)
        os.system('clear')
        print("Please review your feedback:")
        time.sleep(2)
        print(f"Name: {feedback[0]}\n")
        print(f"Feedback: {feedback[1]}\n")
        time.sleep(1)
        user_input = input("Are you happy to proceed with this feedback?\n"
                           "Enter C to Confirm and return to main menu\n" 
                           "Enter D to Delete entries and return to main menu\n"
                           "Enter N to change Name\nEnter F to change Feedback:\n")
        # Check that input is alphabet character only, solution from W3 schools:
        # https://www.w3schools.com/python/ref_string_isalpha.asp#:~:text=The%20isalpha()%20method%20returns,!%23%25%26%3F%20etc
        if not user_input.isalpha():
            print(colored("Invalid entry, please enter C/D/N/ or F to proceed.",
                          'white', 'on_red', ['bold']))
            time.sleep(2)
            # user_input
        elif len(user_input) > 1:
            print((colored("Invalid entry, please enter only 1 character from"
                           "C/D/N/ or F to proceed.", 'white', 'on_red',
                           ['bold'])))
            self.create_feedback
        elif user_input.lower() == "c":
            print("Thanks for the feedback!\n")
            return
        elif user_input.lower() == "d":
            print("Deleting and returning to main menu...")
            self.delete_feedback(row_count)
        elif user_input.lower() == "n":
            self.update_feedback(1, row_count)
        elif user_input.lower() == "f":
            self.update_feedback(2, row_count)
        else:
            print((colored("Invalid entry, please enter only character from"
                           "C/D/N/ or F to proceed.", 'white', 'on_red',
                           ['bold'])))
            self.read_feedback()
            
        return

    def create_feedback(self):
        """
        Request user inputs for name and feeback, perform confirmation step and
        upload to spreadsheet.
        """
        os.system('clear')
        name_input = input("Please enter your name or leave blank to remain"
                           " anonymous:\n")
        if name_input == "":
            name_input = "anonymous"
        feedback_input = input('Please enter your feedback:\n')
        now = d.datetime.now()
        date_input = now.strftime("%d/%m/%Y, %H:%M:%S")
        feedback_data = [name_input, feedback_input, date_input]
        # Add data as row in feedback sheet.
        self.FEEDBACK_SHEET.append_row(feedback_data)



class ForecastWeather():
    """
    Class for user feedback on forecasted weather with associated methods
    """

    def __init__(self, forecast_dictionary, location_dictionary):
        self.forecast_dictionary = forecast_dictionary
        self.location_dictionary = location_dictionary
        
    day_one_parsed = {}
    day_two_parsed = {}
    day_three_parsed = {}

    def parse_forecast(self):

        """
        Function to extract required data from Open Weather API 
        dictionary.
        """

        # Create 3 day forecast by selecting the first three items in the
        # forecast_dictionary.
        day_one = self.forecast_dictionary[0]
        day_two = self.forecast_dictionary[1]
        day_three = self.forecast_dictionary[2]

        keys = [
                'reference_time', 'wind', 'temperature',
                'detailed_status', 'weather_code', 'precipitation_probability'
                ]

        # Dictionary comprehension utilised as opposed to extract data function
        # to clean up code. Solution found on stack overflow:
        # https://stackoverflow.com/questions/3420122/filter-dict-to-contain-only-certain-keys

        self.day_one_parsed = {key: day_one[key] for key in keys}
        self.day_two_parsed = {key: day_two[key] for key in keys}
        self.day_three_parsed = {key: day_three[key] for key in keys}

        return

    def create_forecast(self, forecast_dict):
        """
        Method to create weather report by printing off the weather
        report obtained via API.
        """

        def return_date_format(timestamp):
            """
            Helper function to create a date from timestamp provided by
            Open Weather API.
            """
            date = d.datetime.fromtimestamp(timestamp).strftime('%d-%m-%y')
            return (date)

        forecast_date = return_date_format(forecast_dict['reference_time'])
        # Delete 273 from temperatures to account for units in deg Kelvin
        day_temp = round(forecast_dict['temperature']['feels_like_day']
                            - 273, 2)
        night_temp = round(forecast_dict['temperature']['feels_like_night']
                            - 273, 2)

        # calculate wind direction cardinal and ordinal directions from
        # degrees
        card_ord_wind_dir = forecast_dict['wind']['deg']

        wind_direction = ""

        if card_ord_wind_dir in np.arange(0, 22.5, 0.5):
            wind_direction = "northerly"
        elif card_ord_wind_dir in np.arange(22.5, 45, 0.5):
            wind_direction = "north-north-easterly"
        elif card_ord_wind_dir in np.arange(45, 67.5, 0.5):
            wind_direction = "north-easterly"
        elif card_ord_wind_dir in np.arange(67.5, 90, 0.5):
            wind_direction = "east-north-easterly"
        elif card_ord_wind_dir in np.arange(90, 112.5, 0.5):
            wind_direction = "easterly"
        elif card_ord_wind_dir in np.arange(112.5, 135, 0.5):
            wind_direction = "east-south-easterly"
        elif card_ord_wind_dir in np.arange(135, 157.5, 0.5):
            wind_direction = "south-easterly"
        elif card_ord_wind_dir in np.arange(157.5, 180, 0.5):
            wind_direction = "south-south-easterly"
        elif card_ord_wind_dir in np.arange(180, 202.5, 0.5):
            wind_direction = "southerly"
        elif card_ord_wind_dir in np.arange(202.5, 225, 0.5):
            wind_direction = "south-south-westerly"
        elif card_ord_wind_dir in np.arange(225, 247.5, 0.5):
            wind_direction = "south-westerly"
        elif card_ord_wind_dir in np.arange(247.5, 270, 0.5):
            wind_direction = "west-south-westerly"
        elif card_ord_wind_dir in np.arange(270, 292.5, 0.5):
            wind_direction = "westerly"
        elif card_ord_wind_dir in np.arange(292.5, 315, 0.5):
            wind_direction = "west-north-westerly"
        elif card_ord_wind_dir in np.arange(315, 337.5, 0.5):
            wind_direction = "north-westerly"
        elif card_ord_wind_dir in np.arange(337.5, 359, 0.5):
            wind_direction = "north-north-westerly"
        elif card_ord_wind_dir == 360:
            wind_direction = "northerly"

        # Calculate wind conditions description from speed and create
        # f string for user feedback that includes the wind direction
        #  information as well.
        wind_speed = forecast_dict['wind']['speed']
        formatted_wind_speed = colored(f"{wind_speed} m/s", 'blue', None,
                                       ['bold'])

        def wind_conditions_string(description):
            """
            Helper function to return string from wind speed description
            passed in from calculation.
            """
            description = colored(description, 'blue', None, ['bold'])
            return (f"There will be {description} with a wind speed"
                    f" of {formatted_wind_speed}. ")

        if wind_speed < 0.5:
            wind_conditions = wind_conditions_string("calm conditions")
        elif wind_speed < 1.5:
            wind_conditions = wind_conditions_string("light air")
        elif wind_speed < 3.3:
            wind_conditions = wind_conditions_string("a light breeze")
        elif wind_speed < 5.5:
            wind_conditions = wind_conditions_string("a gentle breeze")
        elif wind_speed < 7.9:
            wind_conditions = wind_conditions_string("a moderate breeze")
        elif wind_speed < 10.7:
            wind_conditions = wind_conditions_string("a fresh breeze")
        elif wind_speed < 13.8:
            wind_conditions = wind_conditions_string("a strong breeze")
        elif wind_speed < 17.1:
            wind_conditions = wind_conditions_string("moderate gales")
        elif wind_speed < 20.7:
            wind_conditions = wind_conditions_string("fresh gales")
        elif wind_speed < 24.4:
            wind_conditions = wind_conditions_string("strong gales")
        elif wind_speed < 28.4:
            wind_conditions = wind_conditions_string("storm force winds")
        elif wind_speed < 32.6:
            wind_conditions = wind_conditions_string("a violent storm")
        elif wind_speed >= 32.7:
            wind_conditions = wind_conditions_string("hurricane force "
                                                     "winds")
        # add wind directions to wind conditions string"
        formatted_wind_direction = colored(f"{wind_direction}", 'blue', None, ['bold'])
        formatted_bearing = colored(f"{card_ord_wind_dir}°", 'blue', None, ['bold'])
        wind_conditions += ("The wind direction will be "
                            f"{formatted_wind_direction} at "
                            f"{formatted_bearing}.")

        # calculate weather icon from weather code callback and
        # assign appropriate icon ot be printed to terminal.
        weather_icon = ""
        weather_code = forecast_dict['weather_code']

        # Line below for testing the weather const to be removed
        # on final deployment

        # weather_code = 201

        if 200 <= weather_code <= 232:
            weather_icon = const.LIGHTNING
        elif 300 <= weather_code <= 321:
            weather_icon = const.DRIZZLE
        elif 500 <= weather_code <= 511:
            weather_icon = const.RAIN
        elif 512 <= weather_code <= 531:
            weather_icon = const.SHOWERS
        elif 600 <= weather_code <= 622:
            weather_icon = const.SNOW
        elif weather_code == 701 or weather_code == 741:
            weather_icon = const.MIST_FOG
        elif 711 <= weather_code <= 731 or 751 <= weather_code <= 771:
            weather_icon = const.HAZE
        elif weather_code == 781:
            weather_icon = const.TORNADO
        elif weather_code == 800:
            weather_icon = const.CLEAR
        elif 801 <= weather_code <= 803:
            weather_icon = const.CLOUDY
        elif weather_code == 804:
            weather_icon = const.OVERCAST

        formatted_date = colored(forecast_date, 'blue', None, ['bold'])
        formatted_day_temp = colored(f"{day_temp} °C", 'blue', None, ['bold'])
        formatted_night_temp = colored(f"{night_temp} °C", 'blue', None, ['bold'])

        return [formatted_date, weather_icon, formatted_day_temp, 
                formatted_night_temp, wind_conditions]

    def print_forecast_to_console(self, day_number, forecast, coordinates):
        """
        Return forecast to terminal along with the forcast 
        title graphics determined from day number
        """
        # if open weather returns a location print given location to terminal,
        # otherwise return the latitude and longitude.
        if self.location_dictionary:
            location = colored(self.location_dictionary[0]['name'], 'blue', None,
                               ['bold'])
        else:
            colored_latitude = colored(f"{coordinates[0]}°", 'blue', None, ['bold'])
            colored_longitude = colored(f"{coordinates[1]}°", 'blue', None, ['bold'])
            location = f"latitude {colored_latitude} and longitude {colored_longitude}"

        if day_number == 1:
            os.system('clear')
            cprint(const.TODAYS_FORECAST, 'green', None, None)
            time.sleep(4)
        elif day_number == 2:
            os.system('clear')
            cprint(const.TOMORROWS_FORECAST, 'cyan', None, None)
            time.sleep(4)
        else:
            os.system('clear')
            colored
            cprint(const.DAY_AFTER_TOMORROWS_FORECAST, 'light_magenta',
                   None, None)
            time.sleep(4)
        os.system('clear')
        print(f"Here is the weather forecast for {location} on {forecast[0]}")
        time.sleep(3)
        print(forecast[1])
        time.sleep(2)
        print(f"The temperature during the day will feel like"
              f" {forecast[2]}")
        time.sleep(3)
        print(f"At night, the temperature will feel like"
              f" {forecast[3]}")
        time.sleep(3)
        print(forecast[4])
        time.sleep(3)
        return

    def move_to_next_day(self):
        input("\nHit return to see the next day's forcast\n")


class LoadingScreens:
    """
    Class to manage screen loading for
    3 options taking in bool property to determine
    when to stop animation.
    """
    # Idea of using class for loading animation from
    #  stack overflow:
    #  https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-running

    def __init__(self, complete, type):
        self.complete = complete
        self.type = type

    def animate(self):
        os.system('clear')
        if self.type == const.LOADING_CONSTANT:
            for c in itertools.cycle(const.LOADING_LIST):
                if self.complete:
                    break
                cprint('\r' + c, 'red', None, ['bold'])
                time.sleep(0.5)
                os.system('clear')
        elif self.type == const.TITLE_CONSTANT:
            for c in const.TITLE_LIST:
                if self.complete:
                    break
                cprint('\r' + c, 'yellow', None, ['bold'])
                time.sleep(2)
        return