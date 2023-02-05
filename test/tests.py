import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from anagrams import Anagram, read_file_to_list

anagram = Anagram()
target = anagram.naive_anagram_improved

class TestAnagram(unittest.TestCase):
    def test_empty_input(self):
        data = read_file_to_list("../datasets/empty_input.txt")
        print(target)
        result = target(data)
        self.assertEqual(result, [])

if __name__ == 'main':
    unittest.main()