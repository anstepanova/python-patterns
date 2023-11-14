import datetime
import random


class DataProvider:
    @staticmethod
    def get_weather_information():
        weather_data = {
            'temperature': random.randint(10, 25),
            'city': 'Berlin',
            'date': datetime.datetime.now().date(),
        }
        print(weather_data)
        return weather_data


class DataProcessor:
    @staticmethod
    def add_current_data_information(data) -> dict:
        data_with_obtained_at_information = {
            'data': data,
            'obtained_at': datetime.datetime.now(),
        }
        return data_with_obtained_at_information


class ReportGenerator:
    @staticmethod
    def make_report(data) -> str:
        weather_data = data['data']
        report = f"""
        The weather is {weather_data['temperature']} Celsius at {weather_data['date']} in {weather_data['city']}.
        The information was obtained in {data['obtained_at']}. 
        """
        print(report)
        return report


class ReportFacade:
    def __init__(self):
        self.data_provider = DataProvider()
        self.data_processor = DataProcessor()
        self.report_generator = ReportGenerator()

    def obtain_data_and_generate_report(self) -> str:
        weather_data = self.data_provider.get_weather_information()
        extended_data = self.data_processor.add_current_data_information(data=weather_data)
        return self.report_generator.make_report(extended_data)


if __name__ == '__main__':
    report_facade = ReportFacade()
    print(f"The result: {report_facade.obtain_data_and_generate_report()}")


    