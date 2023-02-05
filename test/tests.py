import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from anagrams import Anagram, read_file_to_list

anagram = Anagram(test_caller= True)
target = anagram.naive_anagram_improved

class TestAnagram(unittest.TestCase):
    def assert_equal_unordered_2d_list(self, results, solutions):
        self.assertEqual(len(results), len(solutions))
        for solution in solutions:
            solution_in_results = any(sorted(solution) == sorted(r)
                                      for r in results)
            self.assertTrue(solution_in_results)
    
    def runner(self, filepath, solutions):
        data = read_file_to_list(filepath)
        result = target(data)
        self.assert_equal_unordered_2d_list(result,solutions)
        
    def test_empty_input(self):
        self.runner(filepath="../datasets/empty_input.txt", 
               solutions=[])
    
    def test_only_lowercase(self):
        self.runner(filepath="../datasets/population_lowercase.txt", 
               solutions=[['elin','line']])
    
    def test_no_anagram(self):
        self.runner(filepath="../datasets/population_no_anagram.txt", 
               solutions=[])
    
    def test_only_duplicates(self):
        self.runner(filepath="../datasets/population_only_duplicates.txt", 
               solutions=[])

if __name__ == 'main':
    unittest.main()