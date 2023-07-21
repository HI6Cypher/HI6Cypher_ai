from API_HI6 import DownloadData
def DataProcessing_myipinfo() :
    url = "https://get.geojs.io/v1/ip/geo.json"
    download = DownloadData(url, "json")
    data = download.GetData()
    if data == 503 :
        return "No connection to Internet!"
    elif data == 400 :
        return "Invalid URL!"
    elif data == 408 :
        return "Request timed out!"
    else :
        string = "Your IP: %s\nCountry: %s, %s\nTimeZone: %s\nLatitude: %s\nLongitude: %s" \
                % (data["ip"], data["country"], data["region"], data["timezone"], data["latitude"],\
                data["longitude"])
        return string