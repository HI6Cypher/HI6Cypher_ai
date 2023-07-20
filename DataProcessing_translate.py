from API_HI6 import DownloadData
def DataProcessing_translate(fromLan, toLan, text) :
    url = f"https://api.codebazan.ir/translate/?type=json&from={fromLan}&to={toLan}&text={text}"
    download = DownloadData(url, "json")
    data = download.GetData()
    if data == 503 :
        return "No connection to Internet!"
    elif data == 400 :
        return "Invalid URL!"
    elif data == 408 :
        return "Request timed out!"
    else :
        return data["result"]