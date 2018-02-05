import datetime

from discord.ext import commands

from accuweather_api import AccuWeatherAPI
from utils import display_weather, display_temperature, display_wind


class AccuWeatherCommand:
    def __init__(self, bot, accuweather_api_key):
        self.bot = bot
        self.accuweather_api = AccuWeatherAPI(accuweather_api_key)

    @commands.command(pass_context=True, no_pm=True)
    async def current_conditions(self, ctx, *, location_key:str):
        conditions = await self.accuweather_api.get_current_conditions(location_key)
        condition = conditions[0]

        message = ' '.join([
            display_weather(condition),
            display_temperature(condition),
            display_wind(condition),
        ])

        print(datetime.datetime.now(), message)

        await self.bot.delete_message(ctx.message)
        await self.bot.say(message)
