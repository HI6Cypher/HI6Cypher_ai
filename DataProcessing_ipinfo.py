from API_HI6 import DownloadData
def DataProcessing_ipinfo(ip) :
    url = f"http://ip-api.com/json/{ip}"
    download = DownloadData(url, "json")
    data = download.GetData()
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
    elif data == 400 :
        return "Invalid URL!"
    elif data == 408 :
        return "Request timed out!"
    else :
        return Decision()