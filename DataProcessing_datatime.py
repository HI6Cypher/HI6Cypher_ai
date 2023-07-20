from API_HI6 import DownloadData
def DataProcessing_datatime(keyword) :
    url = "http://api.codebazan.ir/time-date/?json=all"
    download = DownloadData(url, "json")
    data = download.GetData()
    def Decision() :
        if keyword == "day" :
            return data["result"]["nameday"]
        elif keyword == "month" :
            return data["result"]["month"]
        elif keyword == "year" :
            return data["result"]["year"]
        elif keyword == "time" :
            return data["result"]["timeen"]
        elif keyword == "date" :
            return data["result"]["dateen"]
        else :
            return "Use keywords [day, month, year, time, date]"
    if data == 503 :
        return "No connection to Internet!"
    elif data == 400 :
        return "Invalid URL!"
    elif data == 408 :
        return "Request timed out!"
    else :
        return Decision()