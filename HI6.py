"""HI6 HTTP Module
~~~
This module uses requests library and http requests methods\n
that written in Python, for Programming World!
### Tools:
 -GetPayload\n
 -PostPayload\n
 -PutPayload\n
 -PatchPayload\n
 -DeletePaylaod\n
~~~
GitHub : <https://github.com/HI6Cypher>
Email : <huaweisclu31@hotmail.com>"""

import requests

class GetPayload :
    """HI6 : GetPayload
    ~~~
    ### This module takes arguments:\n
    url, mode, data, json, params, headers, files, auth, proxies, timeout(default: 15s)
    ### example code:
    >>> from HI6 import GetPayload
    >>> getting = GetPayload("url = https://api.example.com", mode = "json")
    >>> data = get_data()
    >>> code = getting.status_code
    >>> print(code)
    >>> 200
    """
    def __init__(self, url, mode, data = None, json = None, params = None, \
                headers = None, files = None, auth = None, proxies = None, timeout = 15) :
        self.__url = str(url)
        self.__mode = str(mode)
        self.__payload = data
        self.__json = json
        self.__params = params
        self.__headers = headers
        self.__files = files
        self.__auth = auth
        self.__proxies = proxies
        self.__timeout = timeout
        self.__status_code = None
        self.__data = None

    @property
    def status_code(self) :
        return self.__status_code

    def __get_data(self) :
        try :
            data = requests.get(url = self.__url, params = self.__params, \
                                data = self.__payload, json = self.__json, \
                                headers = self.__headers, files = self.__files, \
                                auth = self.__auth, proxies = self.__proxies, \
                                timeout = self.__timeout)
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
        except requests.exceptions.Timeout :
            self.__data = 408
            self.__status_code = 408
        except requests.exceptions.MissingSchema :
            self.__data = 400
            self.__status_code = 400
        except requests.exceptions.ChunkedEncodingError:
            self.__data = 400
            self.__status_code = 400
        except requests.exceptions.InvalidURL :
            self.__data = 400
            self.__status_code = 400
        except requests.exceptions.ContentDecodingError :
            self.__data = 500
            self.__status_code = 500
        except requests.exceptions.JSONDecodeError :
            raise ValueError(f"({self.__mode}) is wrong value!, change your mode")
        except :
            self.__data = 404
            self.__status_code = 404

    def get_data(self) :
        """ GetPayload : get_data
        ~~~
        503 -> Service Unavailable\n
        500 -> Internal Server Error\n
        408 -> Request Timeout\n
        404 -> Not Found (or something went wronge)\n
        400 -> Bad Request (probably due to invalid URL)
        """
        self.__get_data()
        if self.__data :
            return self.__data
        else :
            return None


class PostPayload :
    """HI6 : PostPayload
    ~~~
    ### This module takes arguments:\n
    url, data, json, params, headers, files, auth, proxies, timeout(default: 15s)
    ### example code:
    >>> from HI6 import PostPayload
    >>> payload = {"key1" : "value1", "key2" : "value2"}
    >>> posting = PostPayload("url = https://api.example.com", data = payload)
    >>> data = post_data()
    >>> code = posting.status_code
    >>> print(code)
    >>> 201
    """
    def __init__(self, url, data, json = None, params = None, \
                headers = None, files = None, auth = None, proxies = None, timeout = 15) :
        self.__url = url
        self.__payload = data
        self.__json = json
        self.__params = params
        self.__headers = headers
        self.__files = files
        self.__auth = auth
        self.__proxies = proxies
        self.__timeout = timeout
        self.__status_code = None
        self.__data = None
    
    @property
    def status_code(self) :
        return self.__status_code

    def __post_data(self) :
        try :
            data = requests.post(url = self.__url, data = self.__payload, \
                                json = self.__json, params = self.__params, \
                                headers = self.__headers, files = self.__files, \
                                auth = self.__auth, proxies = self.__proxies, \
                                timeout = self.__timeout)
            self.__status_code = data.status_code
        except requests.exceptions.ConnectionError :
            self.__data = 503
            self.__status_code = 503
        except requests.exceptions.Timeout :
            self.__data = 408
            self.__status_code = 408
        except requests.exceptions.MissingSchema :
            self.__data = 400
            self.__status_code = 400
        except requests.exceptions.ChunkedEncodingError:
            self.__data = 400
            self.__status_code = 400
        except requests.exceptions.InvalidURL :
            self.__data = 400
            self.__status_code = 400
        except requests.exceptions.ContentDecodingError :
            self.__data = 500
            self.__status_code = 500
        except :
            self.__data = 404
            self.__status_code = 404
        else :
            self.__data = data.text

    def post_data(self) :
        """ PostPayload : post_data
        ~~~
        503 -> Service Unavailable\n
        500 -> Internal Server Error\n
        408 -> Request Timeout\n
        404 -> Not Found (or something went wronge)\n
        400 -> Bad Request (probably due to invalid URL)
        """
        self.__post_data()
        if self.__data :
            return self.__data
        else :
            return None


class PutPaylaod :
    """HI6 : PutPaylaod
    ~~~
    ### This module takes arguments:\n
    url, data, json, params, headers, files, auth, proxies, timeout(default: 15s)
    ### example code:
    >>> from HI6 import PutPaylaod
    >>> payload = {"key1" : "value1", "key2" : "value2"}
    >>> putting = PutPaylaod("url = https://api.example.com", data = payload)
    >>> data = put_data()
    >>> code = putting.status_code
    >>> print(code)
    >>> 200
    """
    def __init__(self, url, data = None, json = None, params = None, \
                headers = None, files = None, auth = None, proxies = None, timeout = 15) :
        self.__url = str(url)
        self.__payload = data
        self.__json = json
        self.__params = params
        self.__headers = headers
        self.__files = files
        self.__auth = auth
        self.__proxies = proxies
        self.__timeout = timeout
        self.__status_code = None
        self.__data = None

    @property
    def status_code(self) :
        return self.__status_code

    def __put_data(self) :
        try :
            data = requests.put(url = self.__url, data = self.__payload, \
                                json = self.__json, params = self.__params, \
                                headers = self.__headers, files = self.__files, \
                                auth = self.__auth, proxies = self.__proxies, \
                                timeout = self.__timeout)
            self.__status_code = data.status_code
        except requests.exceptions.ConnectionError :
            self.__data = 503
            self.__status_code = 503
        except requests.exceptions.Timeout :
            self.__data = 408
            self.__status_code = 408
        except requests.exceptions.MissingSchema :
            self.__data = 400
            self.__status_code = 400
        except requests.exceptions.ChunkedEncodingError:
            self.__data = 400
            self.__status_code = 400
        except requests.exceptions.InvalidURL :
            self.__data = 400
            self.__status_code = 400
        except requests.exceptions.ContentDecodingError :
            self.__data = 500
            self.__status_code = 500
        except :
            self.__data = 404
            self.__status_code = 404
        else :
            self.__data = data.text

    def put_data(self) :
        """ PutPaylaod : put_data
        ~~~
        503 -> Service Unavailable\n
        500 -> Internal Server Error\n
        408 -> Request Timeout\n
        404 -> Not Found (or something went wronge)\n
        400 -> Bad Request (probably due to invalid URL)
        """
        self.__put_data()
        if self.__data :
            return self.__data
        else :
            return None


class PatchPayload :
    """HI6 : PatchPayload
    ~~~
    ### This module takes arguments:\n
    url, data, json, params, headers, files, auth, proxies, timeout(default: 15s)
    ### example code:
    >>> from HI6 import PatchPayload
    >>> payload = {"key1" : "value2"}
    >>> patching = PatchPayload("url = https://api.example.com", data = payload)
    >>> data = patch_data()
    >>> code = patching.status_code
    >>> print(code)
    >>> 200
    """
    def __init__(self, url, data = None, json = None, params = None, \
                headers = None, files = None, auth = None, proxies = None, timeout = 15) :
        self.__url = str(url)
        self.__payload = data
        self.__json = json
        self.__params = params
        self.__headers = headers
        self.__files = files
        self.__auth = auth
        self.__proxies = proxies
        self.__timeout = timeout
        self.__status_code = None
        self.__data = None

    @property
    def status_code(self) :
        return self.__status_code

    def __patch_data(self) :
        try :
            data = requests.patch(url = self.__url, data = self.__payload, \
                                json = self.__json, params = self.__params, \
                                headers = self.__headers, files = self.__files, \
                                auth = self.__auth, proxies = self.__proxies, \
                                timeout = self.__timeout)
            self.__status_code = data.status_code
        except requests.exceptions.ConnectionError :
            self.__data = 503
            self.__status_code = 503
        except requests.exceptions.Timeout :
            self.__data = 408
            self.__status_code = 408
        except requests.exceptions.MissingSchema :
            self.__data = 400
            self.__status_code = 400
        except requests.exceptions.ChunkedEncodingError:
            self.__data = 400
            self.__status_code = 400
        except requests.exceptions.InvalidURL :
            self.__data = 400
            self.__status_code = 400
        except requests.exceptions.ContentDecodingError :
            self.__data = 500
            self.__status_code = 500
        except :
            self.__data = 404
            self.__status_code = 404
        else :
            self.__data = data.text

    def patch_data(self) :
        """ PatchPayload : patch_data
        ~~~
        503 -> Service Unavailable\n
        500 -> Internal Server Error\n
        408 -> Request Timeout\n
        404 -> Not Found (or something went wronge)\n
        400 -> Bad Request (probably due to invalid URL)
        """
        self.__patch_data()
        if self.__data :
            return self.__data
        else :
            return None


class DeletePayload :
    """HI6 : DeletePayload
    ~~~
    ### This module takes arguments:\n
    url, data, json, params, headers, files, auth, proxies, timeout(default: 15s)
    ### example code:
    >>> from HI6 import DeletePayload
    >>> payload = {"key1" : "value2"}
    >>> deleting = DeletePayload("url = https://api.example.com", data = payload)
    >>> data = delete_data()
    >>> code = deleting.status_code
    >>> print(code)
    >>> 204
    """
    def __init__(self, url, data = None, json = None, params = None, \
                headers = None, files = None, auth = None, proxies = None, timeout = 15) :
        self.__url = str(url)
        self.__payload = data
        self.__json = json
        self.__params = params
        self.__headers = headers
        self.__files = files
        self.__auth = auth
        self.__proxies = proxies
        self.__timeout = timeout
        self.__status_code = None
        self.__data = None

    @property
    def status_code(self) :
        return self.__status_code

    def __delete_data(self) :
        try :
            data = requests.delete(url = self.__url, data = self.__payload, \
                                json = self.__json, params = self.__params, \
                                headers = self.__headers, files = self.__files, \
                                auth = self.__auth, proxies = self.__proxies, \
                                timeout = self.__timeout)
            self.__status_code = data.status_code
        except requests.exceptions.ConnectionError :
            self.__data = 503
            self.__status_code = 503
        except requests.exceptions.Timeout :
            self.__data = 408
            self.__status_code = 408
        except requests.exceptions.MissingSchema :
            self.__data = 400
            self.__status_code = 400
        except requests.exceptions.ChunkedEncodingError:
            self.__data = 400
            self.__status_code = 400
        except requests.exceptions.InvalidURL :
            self.__data = 400
            self.__status_code = 400
        except requests.exceptions.ContentDecodingError :
            self.__data = 500
            self.__status_code = 500
        except :
            self.__data = 404
            self.__status_code = 404
        else :
            self.__data = data.text

    def delete_data(self) :
        """ DeletePayload : delete_data
        ~~~
        503 -> Service Unavailable\n
        500 -> Internal Server Error\n
        408 -> Request Timeout\n
        404 -> Not Found (or something went wronge)\n
        400 -> Bad Request (probably due to invalid URL)
        """
        self.__delete_data()
        if self.__data :
            return self.__data
        else :
            return None