from DataClass import DataClass
from DataProcessing import *
def Interface_myipinfo() :
    return DataProcessing_myipinfo()

def Interface_passwordgenerator(length) :
    return "your password is: %s" % (DataProcessing_passwordgenerator(length))

def Interface_translate(fromLan, toLan, text) :
    if text :
        lans = DataClass.languages
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

def Interface_weather(lat = None, lon = None, timezone = "UTC") :
    if lat and lon and timezone :
        if timezone.title() in DataClass.timezones :
            return DataProcessing_weather(lat, lon, timezone)
        else :
            return DataProcessing_weather(lat, lon, timezone = "UTC")
    else :
        return DataProcessing_weather()

