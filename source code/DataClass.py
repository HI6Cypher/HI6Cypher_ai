import json

class DataClass :
    @staticmethod
    def openfile(path, param) :
        with open(path, "r") as file :
            reader = json.load(file)
        return reader[param]

    def keywords(keyword) :
        return DataClass.openfile("keywords.json", keyword)

    def proxies() :
        return DataClass.openfile("proxies.json", "proxies")

    def languages() :
        return DataClass.openfile("languageslist.json", "languages")

    def timezones() :
        return DataClass.openfile("timezones.json", "timezones")