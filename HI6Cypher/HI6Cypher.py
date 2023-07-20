import json
import os
class HI6Cypher :
    """HI6Cypher
    ~~~
    ### HI6Cypher is a module for Encription in Programming World.\n
    ~~~
    Classes:
    ~~~
    for Encripting your data -> Encription(username, data)\n
    for Decripting your data -> Decription(username)\n
    for Deleting your data -> DeleteData(username)\n
    for Show ASCII Art -> ASCIIArt()\n
    \n
    ~~~
    ### Note: your data must be in this range:\n
    ### Alphabet, Numbers, Symbols(<@?_*=;!+-:.$> )
    """
    def __init__(self, username, data) :
        self._username = username
        self._data = str(data)
        self.__file_path = f"C:\Program Files\\{self._username}.json"
        self._encription_text = ""
        self._decription_text = ""
        self._load_text = ""
        
    def SaveToFile(self) :
        try :
            with open(self.__file_path, "w") as file :
                json.dump(self._encription_text, file)
        except FileNotFoundError :
            raise FileNotFoundError("HI6Cypher can't find the file!")
    def ReadFromFile(self) :
        try :
            with open(self.__file_path, "r") as file :
                try :
                    self._load_text = json.load(file)
                except json.decoder.JSONDecodeError :
                    self._decription_text = None
        except FileNotFoundError :
            self._decription_text = None

    def __repr__(self) :
        return f"{self._username} : {self._data}"


class Encription(HI6Cypher) :
    """HI6Cypher : Encription
    ~~~
    ### Encription Class encripts your data in username framework.\n
    ~~~
    Encripting Data:
    ~~~
    >>> my_data = Encription("my_data", "HI6Cypher")
    >>> my_data.Encript()
    Now our data has been Ecripted.\n
    """
    def __init__(self, username, data) :
        super().__init__(username, data)
        self.__encription = {"A" : "!_", "B" : "?;", "C" : "+;", "D" : "!;", "E" : "?<", "F" : "+<",
        "G" : "!<", "H" : "?:", "I" : "+:", "J" : "!:", "K" : "?>", "L" : "+>", "M" : "!>",
        "N" : "?-", "O" : "!-", "P" : "+-", "Q" : "?$", "R" : "+$", "S" : "!$", "T" : "??",
        "U" : "+?", "V" : "!?", "W" : "$;", "X" : "$:", "Y" : "*_", "Z" : "@_", "a" : "*;",
        "b" : "@;", "c" : "=_", "d" : "*>", "e" : "*<", "f" : "@<", "g" : "=;", "h" : "*:",
        "i" : "@:", "j" : "=<", "k" : "@>", "l" : "=:", "m" : "*-", "n" : "@-", "o" : "=>",
        "p" : "*$", "q" : "@$", "r" : "=-", "s" : "*?", "t" : "@?", "u" : "=$", "v" : "$_",
        "w" : "$<", "x" : "=?", "y" : "?_", "z" : "+_", "0" : "<!>", "1" : "<@>", "2" : "<?>",
        "3" : "<+>", "4" : "<$>", "5" : "<:>", "6" : "<*>", "7" : "<=>", "8" : "<;>", "9" : "<_>",
        ":" : "@*", "." : "=*", ";" : "._", "_" : ".$", "-" : "$$", "!" : ".;", "*" : ".?", "<" : "$?",
        "@" : ".<", "=" : "$>", ">" : "$*", "?" : ".>", "+" : "$-", "$" : "?*"}

    def Encript(self) :
        """### This method will Encript you data."""
        for i in list(self._data) :
            try :
                self._encription_text += f"{self.__encription[i]} "
            except KeyError :
                raise KeyError("HI6Cypher crashed! Wronge character!")
            else :    
                self.SaveToFile()

    def __repr__(self) :
        return f"{self._username} : {self._data}"


class Decription(HI6Cypher) :
    """HI6Cypher : Decription
    ~~~
    ### Decription Class decripts your data in username framework.\n
    ~~~
    Decripting Data:
    ~~~
    >>> my_data = Decription("my_data")
    >>> result = my_data.Decript()
    >>> print(result)
    >>> HI6Cypher
    Now our data has been decripted.
    """
    def __init__(self, username, data = False) :
        super().__init__(username, data)
        self.__encription = {"A" : "!_", "B" : "?;", "C" : "+;", "D" : "!;", "E" : "?<", "F" : "+<",
        "G" : "!<", "H" : "?:", "I" : "+:", "J" : "!:", "K" : "?>", "L" : "+>", "M" : "!>",
        "N" : "?-", "O" : "!-", "P" : "+-", "Q" : "?$", "R" : "+$", "S" : "!$", "T" : "??",
        "U" : "+?", "V" : "!?", "W" : "$;", "X" : "$:", "Y" : "*_", "Z" : "@_", "a" : "*;",
        "b" : "@;", "c" : "=_", "d" : "*>", "e" : "*<", "f" : "@<", "g" : "=;", "h" : "*:",
        "i" : "@:", "j" : "=<", "k" : "@>", "l" : "=:", "m" : "*-", "n" : "@-", "o" : "=>",
        "p" : "*$", "q" : "@$", "r" : "=-", "s" : "*?", "t" : "@?", "u" : "=$", "v" : "$_",
        "w" : "$<", "x" : "=?", "y" : "?_", "z" : "+_", "0" : "<!>", "1" : "<@>", "2" : "<?>",
        "3" : "<+>", "4" : "<$>", "5" : "<:>", "6" : "<*>", "7" : "<=>", "8" : "<;>", "9" : "<_>",
        ":" : "@*", "." : "=*", ";" : "._", "_" : ".$", "-" : "$$", "!" : ".;", "*" : ".?", "<" : "$?",
        "@" : ".<", "=" : "$>", ">" : "$*", "?" : ".>", "+" : "$-", "$" : "?*"}
        self.__decription = {v : k for k, v in self.__encription.items()}

    def Decript(self) :
        """### This method will Decript you data."""
        self.ReadFromFile()
        splitter = self._load_text.split()
        for key in splitter :
            self._decription_text += f"{self.__decription[key]}"
        else :
            return self._decription_text

    def __repr__(self) :
        return f"{self._username}"


class DeleteData(HI6Cypher) :
    """HI6Cypher : DeleteData
    ~~~
    ### DeleteData Class deletes your data in username framwork.\n
    ~~~
    Deleting Data:
    ~~~
    >>> my_data = DeleteData("my_data")
    >>> my_data.delete()
    Now your data has been deleted.
    """
    def __init__(self, username, data = False) :
        super().__init__(username, data)
        self.__file_path = f"C:\Program Files\\{self._username}.json"

    def Delete(self) :
        """### This method will Delete your data."""
        try :
            os.remove(self.__file_path)
        except FileNotFoundError :
            raise FileNotFoundError("HI6Cypher can't find the file!")

    def __repr__(self) :
        return f"{self._username}"


class ASCIIArt(HI6Cypher) :
    """HI6Cypher : ASCIIArt
    ~~~
    ### ASCIIArt Class returns some ASCII Art texts.\n
    ~~~
    Skull face:
    ~~~
    >>> my_art = ASCIIArt()
    >>> skull = my_art.Skull
    >>> print(skull)
    To show Skull face.\n
    ~~~
    HI6Cypher text:
    ~~~
    >>> my_art = ASCIIArt()
    >>> HI6Cypher_text = my_art.Text_HI6Cypher()
    >>> print(HI6Cypher_text)
    To show HI6Cypher text.\n
    ~~~
    Skull face and HI6Cypher text:
    ~~~
    >>> my_art = ASCIIArt()
    >>> art = my_art.Skull_HI6Cypher()
    >>> print(art)
    To show both of them.
    """
    def __init__(self, username = False, data = False) :
        super().__init__(username, data)
        self.__ASCII_skull = """
                              :::!~!!!!!:.
                        .xUHWH!! !!?M88WHX:.
                        .X*#M@$!!  !X!M$$$$$$WWx:.
                    :!!!!!!?H! :!$!$$$$$$$$$$8X:
                    !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
                    :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
                    ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
                    !:~~~ .:!M"T#$$$$WX??#MRRMMM!
                    ~?WuxiW*`   `"#$$$$8!!!!??!!!
                    :X- M$$$$       `"T#$T~!8$WUXU~
                    :%`  ~#$$$m:        ~!~ ?$$$$$$
                :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
        .....   -~~:<` !    ~?T#$$@@W@*?$$      /`
        W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
        #"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
        :::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
        .~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
        Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
        $R@i.~~ !     :   ~$$$$$B$$en:``
        ?MXT@Wx.~-~-~:     ~"##*$$$$M~
        """
        self.__ASCII_HI6Cypher_text = """
         _    _ _____  __   _____            _               
        | |  | |_   _|/ /  / ____|          | |              
        | |__| | | | / /_ | |    _   _ _ __ | |__   ___ _ __ 
        |  __  | | ||  _ \| |   | | | |  _ \|  _ \ / _ \  __|
        | |  | |_| || (_) | |___| |_| | |_) | | | |  __/ |   
        |_|  |_|_____\___/ \_____\__  |  __/|_| |_|\____|   
                                __/ | |                   
                               |___/|_|
        """

    def Skull(self) :
        """This method will show Skull face"""
        return self.__ASCII_skull

    def Text_HI6Cypher(self) :
        """This method will show HI6Cypher text"""
        return self.__ASCII_HI6Cypher_text

    def Skull_HI6Cypher(self) :
        """This method will show Skull face and HI6Cypher text together"""
        return f"{self.__ASCII_skull}\n\n{self.__ASCII_HI6Cypher_text}"