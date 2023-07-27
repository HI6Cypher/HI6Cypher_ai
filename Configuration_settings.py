import configparser
import os
class Configuration :
    """Configuration
    ~~~
    -> Use for saving HI6Cypher settings"""
    def __init__(self, path) :
        self.__path = path

    @property
    def set_config(self) :
        return self.__set_config

    @set_config.setter
    def set_config(self, option, values) :
        self.__set_config(option = option, values = values)

    def __create_config(self) :
        config = configparser.ConfigParser()
        config.add_section("Settings")
        config.set("Settings", "background_color", "white")
        config.set("Settings", "button_color", "blue")
        save_config = open(self.__path, "w")
        config.write(save_config)
        save_config.close()
    
    def __get_config(self) :
        if not os.path.exists(self.__path) :
            self.__create_config()
        config = configparser.ConfigParser()
        config.read(self.__path)
        return config

    def __set_config(self, option, values) :
            config = self.__get_config()
            config.set("Settings", option, values)
            save_config = open(self.__path, "w")
            config.write(save_config)
            save_config.close()




