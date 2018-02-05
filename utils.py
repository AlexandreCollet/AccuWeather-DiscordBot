def display_weather(condition):
    kwargs = {
        'emoji': '\u2600',
        'weather': condition['WeatherText'],
    }
    return '{emoji} {weather}'.format(**kwargs)


def display_temperature(condition):
    kwargs = {
        'emoji': '\U0001F321',
        'value': condition['Temperature']['Metric']['Value'],
        'unit': condition['Temperature']['Metric']['Unit'],
    }
    return '{emoji} {value}°{unit}'.format(**kwargs)


def display_wind(condition):
    kwargs = {
        'emoji': '\U0001F4A8',
        'value': condition['Wind']['Speed']['Metric']['Value'],
        'unit': condition['Wind']['Speed']['Metric']['Unit'],
        'value_gust': condition['WindGust']['Speed']['Metric']['Value'],
        'unit_gust': condition['WindGust']['Speed']['Metric']['Unit'],
    }
    return '{emoji} {value}{unit} {value_gust}{unit_gust}'.format(**kwargs)
