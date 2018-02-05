# AccuWeather-DiscordBot

A really simple bot to display current conditions for a specific location.

![accuweather_discordbot](https://user-images.githubusercontent.com/3273308/35831018-8988d4e8-0ac8-11e8-8565-21f9f889ad74.gif)

## Usage

Commands for this bot follow this structure: `@AccuWeatherBotName command [argument]`.

| Command | Description |
|---------|-------------|
| `@AccuWeatherBotName current_conditions [location_key]` | Display current conditions for a specific location. |

## Installation

### With Docker

The easiest way to run this bot is through Docker with this command:

```
$ docker run --env DISCORD_TOKEN=*** --env ACCUWEATHER_API_KEY=*** raftorn/accuweather-discordbot
```

### Manually

Otherwise, you can run the following commands:

```
$ git clone https://github.com/AlexandreCollet/AccuWeather-DiscordBot.git
$ cd AccuWeather-DiscordBot
$ pip3 install -r requirements.txt
$ vim settings.py
$ python3 main.py
```

## Configuration

- `DISCORD_TOKEN`: Secret token of your discord bot application
- `ACCUWEATHER_API_KEY`: Your personal AccuWeather API Key
- (optional) `LANGUAGE`: String indicating the language in which to return the messages. The complete list [here](https://developer.accuweather.com/localizations-by-language).
