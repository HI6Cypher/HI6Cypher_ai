from API_HI6 import DownloadData
def DataProcessing_translate(fromLan, toLan, text) :
    url = f"https://api.codebazan.ir/translate/?type=json&from={fromLan}&to={toLan}&text={text}"
    download = DownloadData(url, "json")
    if download.GetData() == 503 :
        return "No connection to Internet!"
    elif download.GetData() == 400 :
        return "Invalid URL!"
    elif download.GetData() == 408 :
        return "Request timed out!"
    else :
        return download.GetData()["result"]