from ex_2 import *
import unittest

class ExTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()

    def testShouldReturnNumberForOne(self):
        
        self.assertEquals(2, self.calc.run([2]))
    
    def testShouldReturnOddWithoutPair(self):
        
        self.assertEquals(1, self.calc.run([2,2,1]))




if __name__ == '__main__':
        unittest.main()
