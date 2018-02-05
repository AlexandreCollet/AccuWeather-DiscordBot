from discord.ext import commands

import settings
from accuweather_command import AccuWeatherCommand


bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'))
bot.add_cog(AccuWeatherCommand(bot, settings.ACCUWEATHER_API_KEY, settings.LANGUAGE))

@bot.event
async def on_ready():
    print('Bot launched')

bot.run(settings.DISCORD_TOKEN)
