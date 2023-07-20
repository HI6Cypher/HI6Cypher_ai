from HI6Cypher import *
import unittest
class TestHI6Cypher(unittest.TestCase) :
    def setUp(self) :
        self.encription_username = {"Python" : "hkawfbskd", "C" : "hhsooso32-9dh",
        "Java" : "$JB*hgos_+", "Cplusplus" : "321", "CSharp" : "urf", "Assembley" : "1-09485"}
        self.decription_data = ["hkawfbskd", "hhsooso32-9dh", "$JB*hgos_+", "321", "urf", "1-09485"]

    def test_decription(self) :
        for v, k in self.encription_username.items() :
            my_encript_data = Encription(v, k)
            my_encript_data.Encript()
            my_decript_data = Decription(v)
            result = my_decript_data.Decript()
            for _ in self.encription_username :
                self.assertIn(result , self.decription_data)

    def test_text__repr__(self) :
        for v, k in self.encription_username.items() :
            my_data = HI6Cypher(v, k)
            my_encript_data = Encription(v, k)
            my_decript_data = Decription(v)
            my_delete_data = DeleteData(v)
            self.assertEqual(str(my_data), f"{v} : {k}")
            self.assertEqual(str(my_encript_data), f"{v} : {k}")
            self.assertEqual(str(my_decript_data), f"{v}")
            self.assertEqual(str(my_delete_data), f"{v}")

    def test_delete(self) :
        for i in self.encription_username :
            my_data = DeleteData(i)
            my_data.Delete()
    
if __name__ == "__main__" :
    unittest.main()