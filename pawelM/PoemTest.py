import unittest
from Poem import *

class PoemTest(unittest.TestCase):
    def setUp(self):
        self.poem = Poem()
    def testShouldCostTam(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()