import unittest
from Poem import *

class TestPoemTest(unittest.TestCase):
    def setUp(self):
	print("dupa")

    def test_testShouldReturnEmptyListWhenFileIsEmpty(self):
	listOfLines = getListOfNonEmptyLines("allEmptyLines.txt")
	self.assertEqual(0, len(listOfLines), "List should be empty")
	unittest.assertEqual(0, len(listOfLines), "List should be empty")

if __name__ == '__main__':
    unittest.main()
    print("dupa")
