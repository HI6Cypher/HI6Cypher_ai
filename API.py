import requests
class DownloadData :
    """"""
    def __init__(self, api_url, mode) :
        self.__url = str(api_url)
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
        """"""
        self.__Get_Data()
        if self.__data :
            return self.__data
        else :
            return None