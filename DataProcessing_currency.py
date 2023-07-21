from API_HI6 import DownloadData
def DataProcessing_currency(currency) :
    url = "https://api.coinlore.net/api/tickers/"
    download = DownloadData(url, "json")
    data = download.GetData()
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
    elif data == 400 :
        return "Invalid URL!"
    elif data == 408 :
        return "Request timed out!"
    else :
        return Decision()