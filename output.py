"""takes one entrance and give one output"""
import re
from Interface import *
from DataClass import DataClass

def OutPut(entrance) : #TODO add other functions
    # myipinfo, 
    # passwordgenerator, uselessfacts, quotes, 
    # catfacts, events, dictionary
    """
    -we have Keywords in DataClass to match them\n
    -we have mainKeyword for figuring out what we should call\n
    -we have a lot of if statement to match mainKeyword to Keyword in DataClass\n
    -we have functions that related to Interface functions\n
    """
    error = f"What?!\nI didn't understand [{entrance}]\nCheck orders"
    try :
        entrance = re.sub(r'"', "'", entrance) #for change double quotion to single quotion
    except :
        pass
    try :
        mainKeyword = re.search(r"^.+?(?=\s)|^.+", entrance).group()
    except :
        return "What?!\nCheck orders"

    def news() :
        """This function related to Interface_news()\n
        checks if keyword is exist to return Interface_news() or not"""
        try :
            keyword = re.search(r"(?<=').+(?=')|\S+$", entrance).group()
        except :
            return error
        return Interface_news(keyword)

    def cryptocurrency() :
        """This function related to Interface_cryptocurrency()\n
        checks if keyword is exist to return Interface_cryptocurrency() or not"""
        try :
            keyword = re.search(r"(?<=').+(?=')|\S+$", entrance).group()
        except :
            return error
        return Interface_cryptocurrency(keyword)
    
    def datetime() :
        """This function related to Interface_datetime()\n
        checks if keyword is exist to return Interface_datetime() or not"""
        return Interface_datatime(mainKeyword.lower())

    def ipinfo() :
        """This function related to Interface_ipinfo()\n
        checks if keyword is exist to return Interface_ipinfo() or not"""
        try :
            ip = re.search(r"\d.*\d", entrance).group()
        except :
            return error
        return Interface_ipinfo(ip)

    def movieinfo() : 
        """This function related to Interface_movieinfo()\n
        checks if keyword is exist to return Interface_movieinfo() or not"""
        try :
            moviename = re.search(r"(?<=').+(?=')|\S+$", entrance).group()
        except :
            return error
        return Interface_movieinfo(moviename)
        # if moviename has one word, using quotion is optional but
        # if moviename has more than one word, using quotion is mandatory

    def translate() :
        """This function related to Interface_translate()\n
        checks if fromLan, toLan and text keywords are exist to return Interface_translate() or not"""
        try :
            fromLan = re.search(r"(?<=from\s).+(?=\sto)", entrance).group()
            toLan =re.search(r"(?<=to\s).+(?=\s)", entrance).group()
            text = re.search(r"(?<=').+(?=')|\S+$", entrance).group()
        except :
            return error
        return Interface_translate(fromLan, toLan, text)
    
    def weather() :
        """This function related to Interface_weather()\n
        checks if keyword is exist to return Interface_weather() or not"""
        try :
            lat = re.search(r"(?<=\s).+(?=\s\d)", entrance).group()
            lon = re.search(r"(?<=\d\s).+(?=\s)|(?<=\d\s).+", entrance).group()
            checklatlon = True
        except :
            checklatlon = False
        try :
            timezone = re.search(r"\S+$", entrance).group()
            checktz = True
        except :
            checktz = False
        if checklatlon and checktz :
            return Interface_weather(lat, lon, timezone)
        elif checklatlon :
            return Interface_weather(lat, lon)
        else :
            return Interface_weather()

    if mainKeyword in DataClass.keywords("news_keywords") :
        return news()
    if mainKeyword in DataClass.keywords("cryptocurrency_keywords") :
        return cryptocurrency()
    elif mainKeyword in DataClass.keywords("datetime_keywords") :
        return datetime()
    elif mainKeyword in DataClass.keywords("translate_keywords") :
        return translate()
    elif mainKeyword in DataClass.keywords("weather_keywords") :
        return weather()
    elif mainKeyword in DataClass.keywords("ipinfo_keywords") :
        return ipinfo()
    elif mainKeyword in DataClass.keywords("movieinfo_keywords") :
        return movieinfo()
    else :
        return error
    # if statements to checking mainKeywords in DataClass