from API_HI6 import DownloadData
def DataProcessing_sunrisesunset(latitude, longitude, timezone = "UTC") :
    url = f"https://api.sunrisesunset.io/json?lat={latitude}&lng={longitude}&timezone={timezone}"
    download = DownloadData(url, "json")
    data = download.GetData()
    if data == 503 :
        return "No connection to Internet!"
    elif data == 400 :
        return "Invalid URL!"
    elif data == 408 :
        return "Request timed out!"
    else :
        string = "Sunrise: %s\nSunset: %s\nDawn: %s\nDusk: %s\nDay length: %s" \
        % (data["results"]["sunrise"], data["results"]["sunset"], data["results"]["dawn"],\
        data["results"]["dusk"], data["results"]["day_length"])
        return string