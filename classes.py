import datetime as d
import time
import os
from termcolor import colored, cprint
import gspread
from google.oauth2.service_account import Credentials
import numpy as np
import weather_icons as icons

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
        max_temp = data[2]
        min_temp = data[4]
        rain = data[8]
        atmos_pressure = data[9]
        mean_wind_speed = data[10]
        sunshine_duration = data[17]
        sunshine_string = ["were", "hours"]
        # Code below to calculate day of the week from date using 
        # datetime strftime method.
        # Used following tutorial: https://www.programiz.com/python-programming/datetime/strftime
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
        print(f"{self.date} was a {day}.")
        time.sleep(2)
        print(f"On that day at Dublin Airport the maximum temperature was {max_temp}°C and the minimum temperature was {min_temp}°C.")
        time.sleep(3)
        print(f"There {sunshine_string[0]} {sunshine_duration} {sunshine_string[1]} of sunshine with a total rainfall of {rain} mm.")
        time.sleep(3)
        print(f"The mean wind speed for the day was {mean_wind_speed} knots with an atmospheric pressure of {atmos_pressure} mbar.")
        time.sleep(2)
    
    def user_options(self):
        """
        Function to assign 4 options to user on completion
        of past weather code.
        """
        user_input = 0
        print()
        while True:
            try:
                user_input = int(input("Press 1 to return to Main Menu\nPress 2 to look for past weather again\nPress 3 for forecast at your location\nPress 4 to leave feedback\n"))
            except ValueError:
                print(colored(f"Invalid entry, please enter an integer between 1 and 4\n",
                    'white', 'on_red', ['bold']))
                continue
            else:
                if user_input not in range(1, 5):
                    print(colored(f"Invalid entry, please enter an integer between 1 and 4\n",
                        'white', 'on_red',['bold']))
                break
        return user_input


class Feedback:
    """
    Class for user feedback on past weather with associated methods
    """

    def __init__(self):
        print("initialised")

    def upload_feedback(self, data):
        """
        Upload feedback to google spreadsheet.
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
        # Add data as row in feedback sheet.
        FEEDBACK_SHEET.append_row(data)
        print("Feedback uploaded, thank you.\n")
        time.sleep(2)

    def confirm_feedback(self, data):
        """
        function to elicit response from user to ensure name and
        feedback are correct with checks to confirm correct inputs
        with associated user feedback.
        """
        print("Please review your feedback:")
        time.sleep(2)
        print(f"Name: {data[0]}")
        print(f"Feedback: {data[1]}\n")
        time.sleep(1)
        user_input = input("Are you happy to proceed with this feedback?\nEnter Y to submit N to return to main menu or E to redo feedback:\n")
        #Check that input is alphabet character only solution from W3 schools:
        #https://www.w3schools.com/python/ref_string_isalpha.asp#:~:text=The%20isalpha()%20method%20returns,!%23%25%26%3F%20etc.
        if not user_input.isalpha():
            print(colored("Invalid entry, please enter Y/N or E to proceed.",
                    'white', 'on_red', ['bold']))
            self.confirm_feedback(data)
        elif len(user_input) > 1:
            print((colored("Invalid entry, please enter only 1 character from Y/N or E to proceed.",
                    'white', 'on_red', ['bold'])))
            self.confirm_feedback(data)
        elif user_input.lower() == "y":
            print("Thanks for the feedback, updloading...\n")
            self.upload_feedback(data)
        elif user_input.lower() == "n":
            print("Returning to main menu...")
        elif user_input.lower() == "e":
            data[1] = input("Please resubmit your feedback:")
            self.confirm_feedback(data)

    def get_feedback(self):
        """
        Request user inputs for name and feeback, perform confirmation step and 
        upload to spreadsheet.
        """
        os.system('clear')
        name_input = input('Please enter your name or leave blank to remain anonymous:\n')
        if name_input == "":
            name_input = "anonymous"
        feedback_input = input('Please enter your feedback:\n')
        now = d.datetime.now()
        date_input = now.strftime("%d/%m/%Y, %H:%M:%S")
        feedback_data = [name_input, feedback_input, date_input]
        self.confirm_feedback(feedback_data)


class ForecastWeather():
    """
    Class for user feedback on forecasted weather with associated methods
    """

    def __init__(self, forecast_dictionary):
        self.forecast_dictionary = forecast_dictionary

    def parse_forecast(self):

        def return_date_format(timestamp):
            date = d.datetime.fromtimestamp(timestamp).strftime('%d-%m-%y')
            return (date)

        # Create 3 day forecast by selecting the first three items in the 
        # forecast_dictionary.
        day_one = self.forecast_dictionary[0]
        day_two = [self.forecast_dictionary[1]]
        day_three = [self.forecast_dictionary[2]]

        keys = [
                'reference_time', 'sunset_time', 'sunrise_time', 
                'wind', 'temperature', 'detailed_status', 
                'weather_code', 'precipitation_probability'
                ]

        # Dictionary comprehension utilised as opposed to extract data function
        # to clean up code. Solution found on stack overflow:
        # https://stackoverflow.com/questions/3420122/filter-dict-to-contain-only-certain-keys

        day_one = {key: day_one[key] for key in keys}
        print(day_one)

        def create_forecast(forecast_dict):
            """
            Method to create weather report by printing off the weather
            report obtained via API.
            """
            forecast_date = return_date_format(forecast_dict['reference_time'])
            # Delete 273 from temperatures to account for units in deg Kelvin
            day_temp = round(
                                forecast_dict['temperature']['feels_like_day'] 
                                - 273, 2
                            )
            night_temp = round(
                                forecast_dict['temperature']['feels_like_night'] 
                                - 273, 2
                              )

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
            if wind_speed < 0.5:
                wind_conditions = f"Today will be calm with a wind speed of {wind_speed} m/s."
            elif wind_speed < 1.5:
                wind_conditions = f"There will be light air today with a wind speed of {wind_speed} m/s."
            elif wind_speed < 3.3:
                wind_conditions = f"There will be a light breeze today with a wind speed of {wind_speed} m/s."
            elif wind_speed < 5.5:
                wind_conditions = f"There will be a gentle breeze today with a wind speed of {wind_speed} m/s."               
            elif wind_speed < 7.9:
                wind_conditions = f"There will be a moderate breeze today with a wind speed of {wind_speed} m/s."
            elif wind_speed < 10.7:
                wind_conditions = f"There will be a fresh breeze today with a wind speed of {wind_speed} m/s."   
            elif wind_speed < 13.8:
                wind_conditions = f"There will be a strong breeze today with a wind speed of {wind_speed} m/s."   
            elif wind_speed < 17.1:
                wind_conditions = f"There will be a moderate breeze today with a wind speed of {wind_speed} m/s."  

            # add wind directions to wind conditions string"
            wind_conditions += f"The wind direction will be {wind_direction} at {card_ord_wind_dir} degrees." 

            #calculate weather icon from weather code callback and
            # assign appropriate icon ot be printed to terminal.
            weather_icon = ""
            weather_code = forecast_dict['weather_code']
            if weather_code == 804:
                weather_icon = icons.CLOUDY
            print(f"Here is the weather forecast for {forecast_date}")
            print(weather_icon)
            print(f"The temperature during the day will feel like {day_temp}")
            print(f"At night, the temperature will feel like {night_temp}")
            print(wind_conditions)

            return
        
        create_forecast(day_one)


        def return_time_format(timestamps):
            time = [d.datetime.fromtimestamp(timestamp).strftime('%H:%M') for timestamp in timestamps]
            print (time)
        



