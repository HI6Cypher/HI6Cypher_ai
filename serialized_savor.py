import pickle
class Save :
    """For saving data"""
    def serialization(path, object) :
        with open(path, "wb") as file :
            pickle.dump(obj = object, file = file, protocol = 4)

    def deserialization(path) :
        with open(path, "rb") as file :
            return pickle.load(file)