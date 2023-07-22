from DataProcessing_translate import DataProcessing_translate
from DataClass import DataClass
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