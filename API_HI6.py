import requests
class DownloadData :
    """API DownloadData
    ~~~
    DownloadData module receives data from URLs
    ### This module takes two arguments:\n
    url -> takes URL\n
    mode -> takes one of API data modes(json, html, text)\n
    data -> payload\n
    json -> json payload\n
    params -> passing parameters in URLs\n
    headers ->  view the server's response headers\n
    files -> post multipart-encoded file\n
    auth -> use authorization headers\n
    timeout -> stop waiting for a response (default = 15s)
    ### example code:
    >>> from API_HI6 import DownloadData
    >>> get_data = DownloadData("https://api.github.com", "text")
    >>> data = get_data.GetData()
    >>> status_code = result.Status_Code
    >>> print(status_code)
    >>> print(data)
    >>> 200
    >>> "whatever texts"
    """
    def __init__(self, url, mode, data = None, json = None, params = None, \
                headers = None, files = None, auth = None, timeout = 15) :
        self.__url = str(url)
        self.__mode = str(mode)
        self.__payload = data
        self.__json = json
        self.__params = params
        self.__headers = headers
        self.__files = files
        self.__auth = auth
        self.__timeout = timeout
        self.__status_code = None
        self.__data = None

    @property
    def Status_Code(self) :
        return self.__status_code

    def __Get_Data(self) :
        try :
            data = requests.get(url = self.__url, params = self.__params, \
                                data = self.__payload, json = self.__json, \
                                headers = self.__headers, files = self.__files, \
                                auth = self.__auth, timeout = self.__timeout)
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


class UploadData :
    """API UploadData
    ~~~
    UploadData module sends data to URLs
    ### This module takes some arguments:\n
    url -> takes URL\n
    data -> payload\n
    json -> json payload\n
    params -> passing parameters in URLs\n
    headers ->  view the server's response headers\n
    files -> post multipart-encoded file\n
    auth -> use authorization headers\n
    timeout -> stop waiting for a response (default = 15s)
    ### example code:
    >>> from API_HI6 import UploadData
    >>> payload = {
        "name": "arash",
        "job": "programmer"
        } 
    >>> send_data = UploadData("https://reqres.in/api/users", data = payload)
    >>> data = send_data.SendData()
    >>> status_code = result.Status_Code
    >>> print(status_code)
    >>> print(data)
    >>> 201
    >>> {"name":"arash","job":"programmer","id":"615","createdAt":"2023-07-21T10:38:00.252Z"}
    """
    def __init__(self, url, data, json = None, params = None, \
                headers = None, files = None, auth = None, timeout = 15) :
        self.__url = url
        self.__payload = data
        self.__json = json
        self.__params = params
        self.__headers = headers
        self.__files = files
        self.__auth = auth
        self.__timeout = timeout
        self.__status_code = None
        self.__text = None
    
    @property
    def Status_Code(self) :
        return self.__status_code

    def __Send_Data(self) :
        try :
            data = requests.post(url = self.__url, data = self.__payload, \
                                json = self.__json, params = self.__params, \
                                headers = self.__headers, files = self.__files, \
                                auth = self.__auth, timeout = self.__timeout)
            self.__status_code = data.status_code
        except requests.exceptions.ConnectionError :
            self.__text = 503
            self.__status_code = 503
        except requests.exceptions.MissingSchema :
            self.__text = 400
            self.__status_code = 400
        except requests.exceptions.ReadTimeout :
            self.__text = 408
            self.__status_code = 408
        except requests.exceptions.InvalidURL :
            self.__text = 400
            self.__status_code = 400
        else :
            self.__text = data.text
        
    def SendData(self) :
        """ UploadData : SendData
        ~~~
        For send data to anywhere first you should\n
        call this method!\n
        ### what exactly this method returns?
        response data -> when everything going to be well\n
        503 -> it means you have no connection to the Internet\n
        400 -> it means the URL not found (probably due to Invalid URL)\n
        408 -> it means your request timed out becausethe URL have 15s to response\n
        """
        self.__Send_Data()
        if self.__text :
            return self.__text
        else :
            return None