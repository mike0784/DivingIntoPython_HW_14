
import os
import pack.ListDir as ld
import pack.WriteJsonFile as jf
import unittest

result = list()

def work(file: str) -> None:
    """Главная функция. Управляет функциями listDirectories() и writeToJSON
    >>> work(result.json)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'list' object has no attribute 'json'
    >>> work("result.json")
    """
    file = os.getcwd() + "\\" + file
    result = ld.listDirectories("i:\\DOS")
    jf.writeToJSON(result, file)

class TestWork(unittest.TestCase):
    def test_one_work(self):
        self.assertEqual(work(result.json), None)
    
    def test_two_work(self):
        self.assertEqual(work("result.json"), None)



if __name__ == "__main__":
    unittest.main()

