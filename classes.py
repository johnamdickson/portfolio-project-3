import datetime as d
import time
import os
from termcolor import colored, cprint
import gspread
from google.oauth2.service_account import Credentials

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

        reference_time = []
        sunset_time = []
        sunrise_time = []
        temperature_feels_like = []
        detailed_status = []
        weather_code = []
        precipitation_probability = []

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
        day_two = {key: day_two[key] for key in keys}
        day_three = {key: day_three[key] for key in keys}
        print(day_one)

        def extract_data_to_days(daily_forecast_dictionary):
            """
            Method to extract the weather forecast data required from 
            a the daily forecast dictionarys.
            """
            container = {}
            keys = [
                    'reference_time', 'sunset_time', 'sunrise_time', 
                    'forecast_date', 'wind["deg"]', 'temperature["day_feels_like"]', 'detailed_status', 
                    'weather_code', 'precipitation_probability'
                     ]

            day_one = {key: day_one[key] for key in keys}

            # for forecast in forecast_dictionary:

            #     forecast_date = return_date_format(forecast['reference_time'])
            #     container["sunset_time"] = forecast['sunset_time']
            #     container["sunrise_time"] = forecast['sunrise_time']
            #     container.update("forecast_date", forecast_date)
            #     # container.append(forecast['wind']['speed'])
            #     # container.append(forecast['wind']['deg'])
            #     # container.append(forecast['temperature']['feels_like_day'])
            #     # container.append(forecast['detailed_status'])
            #     # container.append(forecast['weather_code'])
            #     # container.append(forecast['precipitation_probability'])
            # return container



        def return_time_format(timestamps):
            time = [d.datetime.fromtimestamp(timestamp).strftime('%H:%M') for timestamp in timestamps]
            print (time)
        



    SUNSHINE = """
                       ▄██▄ 
                       ████
                       ████
       ▄██▄            ████            ▄██▌
       █████▄                        ▄█████
         ▀████                     ▐████▀
           ▀▀▀     ▄▄▓██████▓▄▄     ▀▀▀
                 ▓██████▀▀██████▓
               ▓███▀          ▀████
              ████              ████
 ▄▄▄▄▄▄▄▄    ▐███                ███▌    ▄▄▄▄▄▄▄▄
▓████████    ▓███                ███▌    ████████▌
             ▐███               ▐███▌
              ▀███▄            ▄███▌
               ▀████▄▄      ▄▄████▀
                 ▀██████████████▀
          ▄██▓       ▀▀▀▀▀▀▀▀       ▓██▄
        ▄█████                      █████▄
       █████            ▄▄            █████
        ▀▀             ████             ▀▀
                       ████
                       ████
                        ▀▀
    """
    
    CLOUDY = """
                ▄▄████████████▄▄
              ▄██████▀▀▀  ▀▀▀█████▓▄
            ▄████▀              ▀████
          ▓███▀                  ▀███▄
        ▓███                     ▐████████▓▄
       ▐███                        ▀▀▀▀▀██████▄
    ▄▄████                                ▀████
    ▓██████▀                                  ▀███
   ▄████▀                                       ███▌
   ▐███                                          ▓███
    ▓███                                          ███▌
    ▐███                                         ████
    ▀███▄                                    ▄████▀
     ██████████████████████████████████████████▀
        ▀▀████████████████████████████████▀▀
    """

    RAIN = """
                  ▄▄▄▓████▓▄▄▄
              ▄▓████████████████▓▄
            ▄█████▀          ▀█████▄
          ▄████▀                ▀████
        ▐████                    ███████▓▄▄
        ████                      ▀██████████▄
        ▓███                               ▀████▌
    ▄▓██████                                  ████
    █████▀                                      ███▌
    ████                                         ▓███
    ███                                          ████
    ▐███                                         ▓███
     ████▄                                     ▄████
      ▀█████▓▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▓██████▀
        ▀████████████████████████████████████▀▀
               ▄▄      ▄▄▄      ▄▄       ▄▄
            ███     ▄██▀     ███     ▄███
          ▄██▀     ▓██     ▄██     ▀██▀
         ██▀     ██      ██▀     ███
             ▄██▀              ███
             ██▀             ▄██▀
            ▀▀               ▀▀
    """