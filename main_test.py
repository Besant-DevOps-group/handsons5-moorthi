import unittest
from main import add

class TestCalc(unittest.TestCase):
    def testadd(self):
        return self.assertEqual(add(5,5),10)
    


if __name__=='__main__':
    unittest.main()