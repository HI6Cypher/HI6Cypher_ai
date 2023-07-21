from API_HI6 import DownloadData
def DataProcessing_movieinfo(movie) :
    url = f"http://www.omdbapi.com/?t={movie}&apikey=4cb67dde"
    download = DownloadData(url, "json")
    data = download.GetData()
    
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
    elif data == 400 :
        return "Invalid URL!"
    elif data == 408 :
        return "Request timed out!"
    else :
        return Decision()