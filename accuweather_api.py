from aiohttp import ClientSession


class AccuWeatherAPI:
    API_ROOT = 'http://dataservice.accuweather.com'
    API_VERSION = 'v1'

    def __init__(self, api_key, language=None):
        self.api_key = api_key
        self.language = language

    def _get_params(self, **additional_params):
        params = {'apikey': self.api_key}

        if self.language is not None:
            params['language'] = self.language

        return {**params, **additional_params}

    async def get_current_conditions(self, location_key):
        url = self.API_ROOT + '/currentconditions/v1/' + location_key
        params = self._get_params(details='true')

        async with ClientSession() as session:
            async with session.get(url, params=params) as response:
                return await response.json()
