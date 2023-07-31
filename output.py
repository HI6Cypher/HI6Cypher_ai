import re
from Interface import *
from DataClass import DataClass

def OutPut(entrance) :
    """### takes one entrance and give one output"""
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

    def myipinfo() :
        """This function related to Interface_myipinfo()\n
        checks if keyword is exist to return Interface_myipinfo() or not"""
        return Interface_myipinfo()

    def passwordgenerator() :
        """This function related to Interface_passwordgenerator()\n
        checks if keyword is exist to return Interface_passwordgenerator() or not"""
        try :
            length = re.search(r"\d.", entrance).group()
        except :
            return error + "\nYou should specify length of password"
        return Interface_passwordgenerator(length)

    def uselessfacts() :
        """This function related to Interface_uselessfacts()\n
        checks if keyword is exist to return Interface_uselessfacts() or not"""
        return Interface_uselessfacts()

    def quotes() :
        """This function related to Interface_quotes()\n
        checks if keyword is exist to return Interface_quotes() or not"""
        return Interface_quotes()

    def catfacts() :
        """This function related to Interface_catfacts()\n
        checks if keyword is exist to return Interface_catfacts() or not"""
        return Interface_catfacts()

    def events() :
        """This function related to Interface_events()\n
        checks if keyword is exist to return Interface_events() or not"""
        try :
            day = re.search(r"(?<=/).+(?=$)", entrance).group()
            month = re.search(r"(?<=\s).+(?=/)", entrance).group()
        except :
            return error
        return Interface_events(month, day)

    def dictionary() :
        try :
            keyword = re.search(r"\S+$", entrance).group()
        except :
            return error
        return Interface_dictionary(keyword)

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
    elif entrance in DataClass.keywords("myipinfo_keywords") :
        return myipinfo()
    elif mainKeyword in DataClass.keywords("myipinfo_keywords") :
        return myipinfo()
    elif mainKeyword in DataClass.keywords("passwordgenerator_keywords") :
        return passwordgenerator()
    elif mainKeyword in DataClass.keywords("uselessfacts_keywords") :
        return uselessfacts()
    elif mainKeyword in DataClass.keywords("quotes_keywords") :
        return quotes()
    elif mainKeyword in DataClass.keywords("catfacts_keywords") :
        return catfacts()
    elif mainKeyword in DataClass.keywords("events_keywords") :
        return events()
    elif mainKeyword in DataClass.keywords("dictionary_keywords") :
        return dictionary()
    else :
        return error
    # if statements to checking mainKeywords in DataClass