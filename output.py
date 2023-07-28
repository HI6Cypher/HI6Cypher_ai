"""takes one entrance and give one output"""
import re
from Interface import *
from DataClass import DataClass
def OutPut(entrance) : #TODO add other functions
    """
    -we have Keywords in DataClass to match them\n
    -we have mainKeyword for figuring out what we should call\n
    -we have a lot of if statement to match mainKeyword to Keyword in DataClass\n
    -we have functions that related to Interface functions\n
    """
    try :
        entrance = re.sub(r'"', "'", entrance) #for change double quotion to single quotion
    except :
        pass
    try :
        mainkeyword_news = re.search(r"^.+(?=\s)", entrance).group()
        mainKeyword_cryptocurrency = re.search(r"^.+(?=\s)", entrance).group()
        mainKeyword_translate = re.search(r"^.+?(?=\s)", entrance).group()
        #TODO add another mainkeywords
    except :
        return "What?!\nI didn't understand"

    def news() :
        """This function related to Interface_news()\n
        checks if keyword is exist to return Interface_news() or not"""
        try :
            keyword = re.search(r"(?<=').+(?=')", entrance).group()
        except :
            return "What?!\nI didn't understand"
        return Interface_news(keyword)

    def translate() :
        """This function related to Interface_translate()\n
        checks if fromLan, toLan and text keywords are exist to return Interface_translate() or not"""
        try :
            fromLan = re.search(r"(?<=from\s).+(?=\sto)", entrance).group()
            toLan =re.search(r"(?<=to\s).+(?=\s)", entrance).group()
            text = re.search(r"(?<=').+(?=')", entrance).group()
        except :
            return "What?!\nI didn't understand"
        return Interface_translate(fromLan, toLan, text)

    def cryptocurrency() :
        """This function related to Interface_cryptocurrency()\n
        checks if keyword is exist to return Interface_cryptocurrency or not"""
        try :
            keyword = re.search(r"(?<=').+(?=')", entrance).group()
        except :
            return "What?!\nI didn't understand"
        return Interface_cryptocurrency(keyword)

    # if statements to checking mainKeywords in DataClass
    if mainkeyword_news in DataClass.news_keywords :
        return news()
    elif mainKeyword_cryptocurrency in DataClass.cryptocurrency_keywords :
        return cryptocurrency()
    elif mainKeyword_translate in DataClass.translate_keywords :
        return translate()
    
    else :
        return "What?!\nI didn't understand"