class PastWeather:
    """
    Class for past weather data and methods
    """
    def __init__(self, weather_data):
        self.weather_data = weather_data

    def parse_data(self):
        print(f"here is the weather data {self.weather_data}")
