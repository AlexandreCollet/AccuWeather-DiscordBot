from aiohttp import ClientSession


class AccuWeatherAPI:
    API_ROOT = 'http://dataservice.accuweather.com'
    API_VERSION = 'v1'

    def __init__(self, api_key, language='fr'):
        self.api_key = api_key
        self.language = language

    async def get_current_conditions(self, location_key):
        url = self.API_ROOT + '/currentconditions/v1/' + location_key
        params = {
            'apikey': self.api_key,
            'details': "true",
            'language': self.language
        }

        async with ClientSession() as session:
            async with session.get(url, params=params) as response:
                return await response.json()
