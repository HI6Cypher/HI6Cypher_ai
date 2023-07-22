from DataProcessing_weather import DataProcessing_weather
from DataClass import DataClass
def Interface_weather(lat = None, lon = None, timezone = "UTC") :
    if lat and lon and timezone :
        if timezone.title() in DataClass.timezones :
            return DataProcessing_weather(lat, lon, timezone)
        else :
            return DataProcessing_weather(lat, lon, timezone = "UTC")
    else :
        return DataProcessing_weather()