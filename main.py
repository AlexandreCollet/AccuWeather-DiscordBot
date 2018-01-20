import os
import datetime
import requests
from discord.ext import commands


class AccuWeatherCommand:
    API_ROOT = 'http://dataservice.accuweather.com'
    API_VERSION = 'v1'

    def __init__(self, bot):
        self.bot = bot

        self.language = os.environ.get('ACCUWEATHER_DISCORDBOT_LANGUAGE')
        self.accuweather_api_key = os.environ.get('ACCUWEATHER_API_KEY')

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

    def get_current_conditions(self, location_key):
        url = self.API_ROOT + '/currentconditions/v1/' + location_key
        params = {
            'apikey': self.accuweather_api_key,
            'details': True,
            'language': self.language
        }

        response = requests.get(url=url, params=params)
        return response.json()

    def get_current_conditions_message(self, location_key):
        conditions = self.get_current_conditions(location_key)
        condition = conditions[0]

        return ' '.join([
            self.get_weather_message(condition),
            self.get_temperature_message(condition),
            self.get_wind_message(condition),
        ])


    @commands.command(pass_context=True, no_pm=True)
    async def current_conditions(self, ctx, *, location_key:str):
        message = self.get_current_conditions_message(location_key)
        print(datetime.datetime.now(), message)

        await self.bot.delete_message(ctx.message)
        await self.bot.say(message)


bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'))
bot.add_cog(AccuWeatherCommand(bot))

@bot.event
async def on_ready():
    print('Bot launched')

discord_login_token = os.environ.get('ACCUWEATHER_DISCORDBOT_DISCORD_TOKEN')
bot.run(discord_login_token)
