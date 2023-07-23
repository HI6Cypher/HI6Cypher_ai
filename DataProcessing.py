from API_HI6 import DownloadData
def DataProcessing_news(keywords) :
    payload = {"keywords" : keywords,
                "language" : "en",
                "apiKey" : "asbBfb6qBcdJwSjEvfO35Tdb9SVJVvq5kSud4gWjPw8caKHV"}
    proxies = {"http" : "https://95.56.254.139:3128"}
    url = "https://api.currentsapi.services/v1/search"
    download = DownloadData(url = url, params = payload, proxies = proxies,  mode = "json", timeout = 30)
    data = download.get_data()
    if data == 503 :
        return "No connection to Internet!"
    elif data == 500 :
        return "internal server error!"
    elif data == 400 :
        return "Invalid URL!"
    elif data == 408 :
        return "Request timed out!"
    elif data == None :
        return None
    else :
        string = ""
        for i in data["news"] :
            text = "Title: %s\n\nDescription: %s\n\nAuthor: %s\n\nPublished: %s\n\nURL: %s\n\nImage: %s\n\n\n\n" \
                    % (i["title"], i["description"], i["author"], i["published"], i["url"], i["image"])
            string += text
        else :
            return string

def DataProcessing_currency(currency) :
    url = "https://api.coinlore.net/api/tickers/"
    download = DownloadData(url = url, mode = "json")
    data = download.get_data()
    def Decision() :
        for i in data["data"] :
            if i["name"] == currency.title() :
                string_1 = "Symbol: %s\nName: %s\nRank: %s\n" \
                        % (i["symbol"], i["name"], i["rank"])
                string_2 = "Price USD: %s\nPrice BTC: %s\n" \
                        % (i["price_usd"], i["price_btc"])
                string_3 = "Percent Change(24h): %s\nPercent Change(1h): %s\nPercent Change(7d): %s" \
                        % (i["percent_change_24h"], i["percent_change_1h"], i["percent_change_7d"])
                return string_1 + string_2 + string_3
                break
            else :
                continue
        else :
            return "Unknown Currency"
    if data == 503 :
        return "No connection to Internet!"
    elif data == 500 :
        return "internal server error!"
    elif data == 400 :
        return "Invalid URL!"
    elif data == 408 :
        return "Request timed out!"
    elif data == None :
        return None
    else :
        return Decision()

def DataProcessing_datatime(keywords) :
    url = "http://api.codebazan.ir/time-date/?json=all"
    download = DownloadData(url = url, mode = "json")
    data = download.get_data()
    def Decision() :
        if keywords == "day" :
            return data["result"]["nameday"]
        elif keywords == "month" :
            return data["result"]["month"]
        elif keywords == "year" :
            return data["result"]["year"]
        elif keywords == "time" :
            return data["result"]["timeen"]
        elif keywords == "date" :
            return data["result"]["dateen"]
        else :
            return "Use keywordss [day, month, year, time, date]"
    if data == 503 :
        return "No connection to Internet!"
    elif data == 500 :
        return "internal server error!"
    elif data == 400 :
        return "Invalid URL!"
    elif data == 408 :
        return "Request timed out!"
    elif data == None :
        return None
    else :
        return Decision()

def DataProcessing_ipinfo(ip) :
    url = f"http://ip-api.com/json/{ip}"
    download = DownloadData(url = url, mode = "json")
    data = download.get_data()
    def Decision() :
        
        if data["status"] == "success" :
            string = "Country: %s, %s, %s\nISP: %s\nLatitude: %s\nLongitude: %s" \
                    % (data["country"], data["regionName"], data["city"], data["isp"], data["lat"],\
                    data["lon"])
            return string
        else :
            return data["message"]
    if data == 503 :
        return "No connection to Internet!"
    elif data == 500 :
        return "internal server error!"
    elif data == 400 :
        return "Invalid URL!"
    elif data == 408 :
        return "Request timed out!"
    elif data == None :
        return None
    else :
        return Decision()

def DataProcessing_movieinfo(movie) :
    payload = {"t" : movie, "apikey" : "4cb67dde"}
    url = f"http://www.omdbapi.com/"
    download = DownloadData(url = url, params = payload, mode = "json")
    data = download.get_data()
    def Decision() :
        if data["Response"] == "True" :
            key_list = []
            value_list = ["Title", "Type", "Rated", "Released", "Runtime", "Genre", "Director",
            "Writer", "Actors", "Country", "Language", "Awards", "imdbRating", "imdbVotes", "imdbID", "Plot"]
            for i in value_list :
                key_list.append(data[i])
            else :
                string_1 = "Title: %s\nType: %s\nRated: %s\nReleased: %s\nRuntime: %s\nGenre: %s\nDirector: %s\n" \
                        % (key_list[0], key_list[1], key_list[2], key_list[3], key_list[4], key_list[5], key_list[6])
                string_2 = "Writer: %s\nActors: %s\nCountry: %s\nLanguage: %s\nAwards: %s\nIMDb Rating: %s\nIMDb Votes: %s\nIMDb ID: %s\nPlot: %s\n" \
                        % (key_list[7], key_list[8], key_list[9], key_list[10], key_list[11], key_list[12], key_list[13], key_list[14], key_list[15])
                return string_1 + string_2
        else :
            return data["Error"]
    if data == 503 :
        return "No connection to Internet!"
    elif data == 500 :
        return "internal server error!"
    elif data == 400 :
        return "Invalid URL!"
    elif data == 408 :
        return "Request timed out!"
    elif data == None :
        return None
    else :
        return Decision()

def DataProcessing_myipinfo() :
    url = "https://get.geojs.io/v1/ip/geo.json"
    download = DownloadData(url= url, mode = "json")
    data = download.get_data()
    if data == 503 :
        return "No connection to Internet!"
    elif data == 500 :
        return "internal server error!"
    elif data == 400 :
        return "Invalid URL!"
    elif data == 408 :
        return "Request timed out!"
    elif data == None :
        return None
    else :
        string = "Your IP: %s\nCountry: %s, %s\nTimeZone: %s\nLatitude: %s\nLongitude: %s" \
                % (data["ip"], data["country"], data["region"], data["timezone"], data["latitude"],\
                data["longitude"])
        return string

def DataProcessing_passwordgenerator(length) :
    payload = {"length" : length}
    url = f"http://api.codebazan.ir/password/"
    download = DownloadData(url = url, params = payload, mode = "text")
    data = download.get_data()
    if data == 503 :
        return "No connection to Internet!"
    elif data == 500 :
        return "internal server error!"
    elif data == 400 :
        return "Invalid URL!"
    elif data == 408 :
        return "Request timed out!"
    elif data == None :
        return None
    else :
        return data

def DataProcessing_translate(fromLan, toLan, text) :
    payload = {"type" : "json", "from" : fromLan, "to" : toLan, "text" : text}
    url = f"https://api.codebazan.ir/translate/"
    download = DownloadData(url = url, params = payload, mode = "json")
    data = download.get_data()
    if data == 503 :
        return "No connection to Internet!"
    elif data == 500 :
        return "internal server error!"
    elif data == 400 :
        return "Invalid URL!"
    elif data == 408 :
        return "Request timed out!"
    elif data == None :
        return None
    else :
        return data["result"]

def DataProcessing_weather(lat = None, lon = None, timezone = None) :
    url_1 = "https://get.geojs.io/v1/ip/geo.json"
    download_1 = DownloadData(url = url_1, mode = "json")
    data_1 = download_1.get_data()
    if data_1 == 503 :
        return "No connection to Internet!"
    elif data_1 == 500 :
        return "internal server error!"
    elif data_1 == 400 :
        return "Invalid URL!"
    elif data_1 == 408 :
        return "Request timed out!"
    elif data_1 == None :
        return None
    elif lat and lon and timezone :
        pass
    else :
        lat = data_1["latitude"]
        lon = data_1["longitude"]
        timezone = data_1["timezone"]
    payload_1 = {"lat" : lat, "lon" : lon, "appid" : "d7ac3233b2d88a4c8f01032c02eae2db"}
    url_2 = f"https://api.openweathermap.org/data/2.5/weather"
    payload_2 = {"lat" : lat, "lng" : lon, "timezone" : timezone}
    url_3 = f"https://api.sunrisesunset.io/json"
    download_2 = DownloadData(url = url_2, params = payload_1, mode = "json")
    data_2 = download_2.get_data()
    download_3 = DownloadData(url = url_3, params = payload_2, mode = "json")
    data_3 = download_3.get_data()
    if data_2 == 503 and data_3 == 503 :
        return "No connection to Internet!"
    elif data_2 == 500 and data_3 == 500 :
        return "internal server error!"
    elif data_2 == 400 and data_3 == 400 :
        return "Invalid URL!"
    elif data_2 == 408 and data_3 == 408 :
        return "Request timed out!"
    elif data_2 == None and data_3 == None :
        return None
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

def DataProcessing_uselessfacts() :
    pass #TODO