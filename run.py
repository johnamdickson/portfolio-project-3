import past_weather as past
from classes import PastWeather


def main():
    available_dates = past.find_date_range()
    user_date = past.get_date(available_dates)
    historical_data = past.find_historical_data_row(user_date, available_dates)
    class_test = PastWeather(historical_data, user_date)
    class_test.parse_data()


main()