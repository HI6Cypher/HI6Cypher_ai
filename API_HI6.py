import requests
class DownloadData :
    """API DownloadData
    ~~~
    DownloadData module receives data from URLs
    ### This module takes two arguments:\n
    url -> takes URL\n
    mode -> takes one of API data modes(json, html, text)
    ### example code:
    >>> from API_HI6 import DownloadData
    >>> result = DownloadData("https://api.github.com", "text")
    >>> data = result.GetData()
    >>> status_code = result.Status_Code
    >>> print(status_code)
    >>> print(data)
    >>> 200
        "any data from github"
    """
    def __init__(self, url, mode) :
        self.__url = str(url)
        self.__mode = str(mode)
        self.__status_code = None
        self.__data = None

    @property
    def Status_Code(self) :
        return self.__status_code

    def __Get_Data(self) :
        try :
            data = requests.get(self.__url, timeout= 15)
            self.__status_code = data.status_code
            if self.__mode == "json" :
                self.__data = data.json()
            elif self.__mode == "html" :
                self.__data = data.text
            elif self.__mode == "text" :
                self.__data = data.text
            else :
                raise ValueError(f"({self.__mode}) is wrong value")
        except requests.exceptions.ConnectionError :
            self.__data = 503
            self.__status_code = 503
        except requests.exceptions.MissingSchema :
            self.__data = 400
            self.__status_code = 400
        except requests.exceptions.ReadTimeout :
            self.__data = 408
            self.__status_code = 408
        except requests.exceptions.InvalidURL :
            self.__data = 400
            self.__status_code = 400
        except requests.exceptions.JSONDecodeError :
            raise ValueError(f"({self.__mode}) is wrong value!, change your mode")


    def GetData(self) :
        """ DownloadData : GetData
        ~~~
        For get data from anywhere first you should\n
        call this method!\n
        ### what exactly this method returns?
        data (json, html, text) -> when everything going to be well\n
        503 -> it means you have no connection to the Internet\n
        400 -> it means the URL not found (probably due to Invalid URL)\n
        408 -> it means your request timed out becausethe URL have 15s to response\n
        """
        self.__Get_Data()
        if self.__data :
            return self.__data
        else :
            return None