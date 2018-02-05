import datetime

from discord.ext import commands

from accuweather_api import AccuWeatherAPI


class AccuWeatherCommand:
    def __init__(self, bot, accuweather_api_key):
        self.bot = bot
        self.accuweather_api = AccuWeatherAPI(accuweather_api_key)

    def get_weather_message(self, condition):
        kwargs = {
            'emoji': '\u2600',
            'weather': condition['WeatherText'],
        }
        return '{emoji} {weather}'.format(**kwargs)

    def get_temperature_message(self, condition):
        kwargs = {
            'emoji': '\U0001F321',
            'value': condition['Temperature']['Metric']['Value'],
            'unit': condition['Temperature']['Metric']['Unit'],
        }
        return '{emoji} {value}°{unit}'.format(**kwargs)

    def get_wind_message(self, condition):
        kwargs = {
            'emoji': '\U0001F4A8',
            'value': condition['Wind']['Speed']['Metric']['Value'],
            'unit': condition['Wind']['Speed']['Metric']['Unit'],
            'value_gust': condition['WindGust']['Speed']['Metric']['Value'],
            'unit_gust': condition['WindGust']['Speed']['Metric']['Unit'],
        }
        return '{emoji} {value}{unit} {value_gust}{unit_gust}'.format(**kwargs)

    async def get_current_conditions_message(self, location_key):
        conditions = await self.accuweather_api.get_current_conditions(location_key)
        condition = conditions[0]

        return ' '.join([
            self.get_weather_message(condition),
            self.get_temperature_message(condition),
            self.get_wind_message(condition),
        ])

    @commands.command(pass_context=True, no_pm=True)
    async def current_conditions(self, ctx, *, location_key:str):
        message = await self.get_current_conditions_message(location_key)
        print(datetime.datetime.now(), message)

        await self.bot.delete_message(ctx.message)
        await self.bot.say(message)
