import pickle
class Save :
    """For saving data"""
    def serialization(path, object) :
        try :
            with open(path, "wb") as file :
                pickle.dump(obj = object, file = file, protocol = 4)
        except :
            pass

    def deserialization(path) :
        try :
            with open(path, "rb") as file :
                return pickle.load(file)
        except :
            pass