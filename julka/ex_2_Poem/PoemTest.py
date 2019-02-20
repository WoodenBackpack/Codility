import unittest
from Poem import *

class PoemTest(unittest.TestCase):
    def setUp(self):
        pass
    def testShouldReturnEmptyListWhenFileIsEmpty(self):
        pass
    def testShouldCreateListOfAuthorsAndTitlesFromDirectory(self):
        expectedPoems = [str(Poem("Adam Mickiewicz", "Niepewność", "")), str(Poem("Juliusz Słowacki", "Testament mójI", ""))]
        poems = createPoemsFromDirectory()
        actualPoems = []
        for poem in poems:
            actualPoems.append(str(poem))
        self.assertEqual(expectedPoems, actualPoems)

if __name__ == '__main__':
    unittest.main()
