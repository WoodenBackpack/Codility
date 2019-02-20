import unittest
from Poem import *

class TestPoemTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_ShouldReturnEmptyListWhenFileIsEmpty(self):
        listOfLines = getListOfNonEmptyLines("allEmptyLines.txt")
        self.assertEqual(0, len(listOfLines), "List should be empty")

    def test_ShouldReturnNumberOfNonEmptyLinesFromFileWithoutEmptyLines(self):
        listOfLines = getListOfNonEmptyLines("fiveNonEmptyLines.txt")
        self.assertEqual(5, len(listOfLines), "List should not be empty")

    def test_ShouldReturnNumberOfNonEmptyLinesFromFileWithEmptyLines(self):
        listOfLines = getListOfNonEmptyLines("fiveLinesTwoEmpty.txt")
        self.assertEqual(3, len(listOfLines), "List should not be empty")


if __name__ == '__main__':
    unittest.main()

