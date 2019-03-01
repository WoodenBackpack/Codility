import unittest
from Poem import *

class PoemTest(unittest.TestCase):
    def setUp(self):
        print("setUp")
    def test_should_return_empty_list_when_file_is_empty(self):
        l = getListOfNonEmptyLines("empty.py")
        self.assertEqual(l, [])

if __name__ == '__main__':
    unittest.main()
