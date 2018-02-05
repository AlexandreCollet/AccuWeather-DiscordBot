import os

from discord.ext import commands

from accuweather_command import AccuWeatherCommand


discord_login_token = os.environ.get('ACCUWEATHER_DISCORDBOT_DISCORD_TOKEN')
accuweather_api_key = os.environ.get('ACCUWEATHER_API_KEY')

bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'))
bot.add_cog(AccuWeatherCommand(bot, accuweather_api_key))

@bot.event
async def on_ready():
    print('Bot launched')

bot.run(discord_login_token)
