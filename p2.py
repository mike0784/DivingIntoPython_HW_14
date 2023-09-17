import unittest

from p1 import work

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