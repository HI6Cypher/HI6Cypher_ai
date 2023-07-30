import json

class DataClass :
    @staticmethod
    def openfile(path, param) :
        with open(path, "r") as file :
            reader = json.load(file)
        return reader[param]

    def keywords(keyword) :
        return DataClass.openfile("doc/keywords.json", keyword)

    def proxies() :
        return DataClass.openfile("doc/proxies.json", "proxies")

    def languages() :
        return DataClass.openfile("doc/languageslist.json", "languages")

    def timezones() :
        return DataClass.openfile("doc/timezones.json", "timezones")