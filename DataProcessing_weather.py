from API_HI6 import DownloadData
def DataProcessing_weather(lat = None, lon = None, timezone = None) :
    url_1 = "https://get.geojs.io/v1/ip/geo.json"
    download_1 = DownloadData(url_1, "json")
    data_1 = download_1.GetData()
    if data_1 == 503 :
        return "No connection to Internet!"
    elif data_1 == 400 :
        return "Invalid URL!"
    elif data_1 == 408 :
        return "Request timed out!"
    elif lat and lon and timezone :
        pass
    else :
        lat = data_1["latitude"]
        lon = data_1["longitude"]
        timezone = data_1["timezone"]
    url_2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=d7ac3233b2d88a4c8f01032c02eae2db"
    url_3 = f"https://api.sunrisesunset.io/json?lat={lat}&lng={lon}&timezone={timezone.title()}"
    download_2 = DownloadData(url_2, "json")
    data_2 = download_2.GetData()
    download_3 = DownloadData(url_3, "json")
    data_3 = download_3.GetData()
    if data_2 == 503 and data_3 == 503 :
        return "No connection to Internet!"
    elif data_2 == 400 and data_3 == 400 :
        return "Invalid URL!"
    elif data_2 == 408 and data_3 == 408 :
        return "Request timed out!"
    else :
        city = data_2["name"]
        weather = data_2["weather"][0]["description"]
        sunrise = data_3["results"]["sunrise"]
        sunset = data_3["results"]["sunset"]
        dawn = data_3["results"]["dawn"]
        dusk = data_3["results"]["dusk"]
        daylength = data_3["results"]["day_length"]
        temp_kelvin = data_2["main"]["temp"]
        temp_celcius = round(temp_kelvin - 273.15, 2)
        temp_fahrenheit = round(1.8 * temp_celcius + 32, 2)
        pressure = data_2["main"]["pressure"]
        humidity = data_2["main"]["humidity"]
        wind = data_2["wind"]["speed"]
        string_1 = "City: %s\nWeather: %s\nTemperature in Kelvin: %s\nTemperature in Fahrenheit: %s\nTemperature in Celcius: %s" \
                % (city, weather, temp_kelvin, temp_fahrenheit, temp_celcius)
        string_2 = "\nPressure: %s\nHumidity: %s\nWind: %s Km/h\nSunrise: %s\nSunset: %s\nDawn: %s\nDusk: %s\nDay length: %s" \
                % (pressure, humidity, wind, sunrise, sunset, dawn, dusk, daylength)
        return string_1 + string_2