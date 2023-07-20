from API_HI6 import DownloadData
def DataProcessing_passwordgenerator(length) :
    url = f"http://api.codebazan.ir/password/?length={length}"
    download = DownloadData(url, "text")
    data = download.GetData()
    if data == 503 :
        return "No connection to Internet!"
    elif data == 400 :
        return "Invalid URL!"
    elif data == 408 :
        return "Request timed out!"
    else :
        return data