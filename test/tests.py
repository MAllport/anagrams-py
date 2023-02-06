import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from anagrams import SolveAnagram, read_file_to_list
from typing import List
from time import time

class TestAnagram(unittest.TestCase):
    """Class that holds tests for the implementations

    Args:
        unittest (_type_): "unittest" library base class
    """
    
    @classmethod
    def setUpClass(cls) -> None:
        """Ran only once before the tests are run. Sets the target
        implementation to test
        """
        #cls.target = SolveAnagram.sorted_anagram
        cls.target = SolveAnagram.count_anagram
        #cls.target = SolveAnagram.count_anagram_counter
    
    def assert_equal_unordered_2d_list(self, results: List[List[str]],
                                       solutions: List[List[str]]) \
                                           -> None:
        """Asserts whether two 2D lists are equal when both the outer and inner
        elements are not in the same order. This is because the anagram 
        implementations do not guarantee any specific ordering of anagrams.
        
        If the result:
        1) is the same length as the solution (same number of anagram groups)
        2) encompasses at least the same anagram groups as the solution
        ..we claim they are logically equal
        
        Example:
        [["Line", "Elin"], ["Erik", "Lire"]] should be equal to
        [["Lire", "Erik"], ["Elin", "Line"]]
        
        Downside - the assertTrue statement does not give accurate information
        to the developer whether the algorithm is partially correct but
        incomplete, or is forming the wrong anagrams.

        Args:
            results (List[List[str]]): Result from anagram implementation
            solutions (List[List[str]]): Solution to the problem
        """
        self.assertEqual(len(results), len(solutions))
        for solution in solutions:
            solution_in_results = any(sorted(solution) == sorted(r)
                                      for r in results)
            self.assertTrue(solution_in_results,
                        msg="Implementation is either incomplete or incorrect")
    
    def runner(self, filepath: str, solutions: List[List[str]]) -> int:
        """Runs the tests given a file path to a dataset and the solution

        Args:
            filepath (str): File path to a dataset
            solutions (List[List[str]]): Anagram solutions to the dataset
        
        Returns:
            int: Time to run in seconds
        """
        data = read_file_to_list(filepath)
        
        start_time = time()
        result = self.target(data)
        end_time = time()
        
        self.assert_equal_unordered_2d_list(result,solutions)
        
        return end_time - start_time
    
    """--- START OF TESTS ---"""
        
    def test_empty_input(self) -> None:
        """Tests for correct result when given an empty file
        """
        self.runner(filepath="../datasets/empty_input.txt", 
               solutions=[])
    
    def test_only_lowercase(self) -> None:
        """Tests for correct result when all words are lowercase
        """
        self.runner(filepath="../datasets/population_lowercase.txt", 
               solutions=[['elin','line']])
    
    def test_no_anagram(self) -> None:
        """Tests for correct result when there are no anagrams
        """
        self.runner(filepath="../datasets/population_no_anagram.txt", 
               solutions=[])
    
    def test_only_duplicates(self) -> None:
        """Tests for correct result when there only exists duplicates
        """
        self.runner(filepath="../datasets/population_only_duplicates.txt", 
               solutions=[])
    
    def test_multiple_groups(self) -> None:
        """Tests for the correct result when there
        is an expanded dataset with more than one anagram group
        """
        self.runner(filepath="../datasets/population_more_groups.txt", 
               solutions=[["Kire", "Erik"], ["Elin", "Line"], 
                          ["Stian", "Nista"]])
    
    def test_basecase(self) -> None:
        """Tests the given population.txt input
        """
        self.runner(filepath="../datasets/population.txt", 
               solutions=[['Elin','Line']])
    
    def test_basecase_big_n(self) -> None:
        """Tests a dataset with large number of entries
        
        """
        #self.runner(filepath="../datasets/100x_chars_population_100000.txt", 
        #       solutions=[['Elin'*100,'Line'*100]])
        time = round(self.runner(filepath="../datasets/population_10000000.txt", 
               solutions=[['Elin','Line']]), 4)
        print(time)
        
        
if __name__ == 'main':
    unittest.main()