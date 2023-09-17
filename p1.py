
import os
import pack.ListDir as ld
import pack.WriteJsonFile as jf
import unittest



def work(file: str) -> None:
    """Главная функция. Управляет функциями listDirectories() и writeToJSON
    >>> work(result.json)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'list' object has no attribute 'json'
    >>> work("result.json")
    """
    result = list()
    file = os.getcwd() + "/" + file
    result = ld.listDirectories("i:/DOS")
    print(file)
    jf.writeToJSON(result, file)

class TestWork(unittest.TestCase):
    def test_one_work(self):
        self.assertEqual(work("result"), None)
    
    def test_two_work(self):
        self.assertEqual(work("result.json"), None)
    
    def test_three_work(self):
        self.assertEqual(work("rr"), None)

    def test_four_work(self):
        self.assertEqual(work("pp.json"), None)



if __name__ == "__main__":
    unittest.main(verbosity=2)

