from DataProcessing import *
from DataClass import DataClass

def Interface_news(keywords) :
    try :
        info = DataProcessing_news(keywords)
        if info == "No connection to Internet!" :
            return "No connection to Internet!"
        elif info == "internal server error!" :
            return "internal server error!"
        elif info == "Invalid URL!" :
            return "Invalid URL!"
        elif info == "Request timed out!" :
            return "Request timed out!"
        elif info == "Something went wronge!" :
            return "Something went wronge!"
        else :
            return f"News about: {keywords}\n\n" + DataProcessing_news(keywords)
    except :
        return "Error!"

def Interface_cryptocurrency(cryptocurrency) :
    try :
        return DataProcessing_cryptocurrency(cryptocurrency)
    except :
        return "Error!"

def Interface_datatime(keywords) :
    try :
        return DataProcessing_datatime(keywords)
    except :
        return "Error!"

def Interface_ipinfo(ip) :
    try :
        return DataProcessing_ipinfo(ip)
    except :
        return "Error!"

def Interface_movieinfo(movie) :
    try :
        info = DataProcessing_movieinfo(movie)
        if info == "No connection to Internet!" :
            return "No connection to Internet!"
        elif info == "internal server error!" :
            return "internal server error!"
        elif info == "Invalid URL!" :
            return "Invalid URL!"
        elif info == "Request timed out!" :
            return "Request timed out!"
        elif info == "Something went wronge!" :
            return "Something went wronge!"
        else :
            return f"Information about {movie}:\n\n{info}"
    except :
        return "Error!"

def Interface_myipinfo() :
    try :
        return DataProcessing_myipinfo()
    except :
        return "Error!"

def Interface_passwordgenerator(length) :
    try :
        info = DataProcessing_passwordgenerator(length)
        if info == "No connection to Internet!" :
            return "No connection to Internet!"
        elif info == "internal server error!" :
            return "internal server error!"
        elif info == "Invalid URL!" :
            return "Invalid URL!"
        elif info == "Request timed out!" :
            return "Request timed out!"
        elif info == "Something went wronge!" :
            return "Something went wronge!"
        else :
            return f"your password is: {DataProcessing_passwordgenerator(length)}"
    except :
        return "Error!"

def Interface_translate(fromLan, toLan, text) :
    try :
            if text :
                lans = DataClass.languages()
                for i in lans :
                    if fromLan.title() == i["name"] :
                        codename_1 = i["code"]
                        break
                    else :
                        continue
                else :
                    return "Unknown Languages"
                for j in lans : 
                    if toLan.title() == j["name"] :
                        codename_2 = j["code"]
                        break
                    else :
                        continue
                else :
                    return "Unknown Languages"

                return DataProcessing_translate(codename_1, codename_2, text)
            else :
                return "Your text is empty"
    except :
        return "Error!"

def Interface_weather(lat = None, lon = None, timezone = "UTC") :
    try :
        if lat and lon and timezone :
            if timezone.title() in DataClass.timezones() :
                return DataProcessing_weather(lat, lon, timezone)
            else :
                return DataProcessing_weather(lat, lon, timezone = "UTC")
        else :
            return DataProcessing_weather()
    except :
        return "Error!"

def Interface_uselessfacts() :
    try :
        info = DataProcessing_uselessfacts()
        if info == "No connection to Internet!" :
            return "No connection to Internet!"
        elif info == "internal server error!" :
            return "internal server error!"
        elif info == "Invalid URL!" :
            return "Invalid URL!"
        elif info == "Request timed out!" :
            return "Request timed out!"
        elif info == "Something went wronge!" :
            return "Something went wronge!"
        else :
            return f"A useless fact:\n{DataProcessing_uselessfacts()}"
    except :
        return "Error!"

def Interface_quotes() :
    try :
        return DataProcessing_quotes()
    except :
        return "Error!"

def Interface_catfacts() :
    try :
        return DataProcessing_catfacts()
    except :
        return "Error!"

def Interface_events(month, day) :
    try :
        return DataProcessing_events(month, day)
    except :
        return "Error!"

def Interface_dictionary(word) :
    try :
        return DataProcessing_dictionary(word)
    except :
        return "Error!"