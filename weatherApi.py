import pyowm

def weatherInfo():
    owm = pyowm.OWM('6f05ee719379d73c2bac55e0832a4289')
    observation = owm.weather_at_place('Cape Coast,Ghana')
    w = observation.get_weather()

    w.get_wind()
    w.get_humidity()
