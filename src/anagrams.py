from collections import defaultdict, Counter
from typing import List, DefaultDict


class Anagram:
    """The class holds all algorithmic implementations of solving the
    anagram problem, as well as helper methods
    """
    def __init__(self, stdout: bool):
        """Determines whether algorithms will write to standard output. 
        Should be "false" during tests.

        Args:
            stdout (bool): Writes results to standard output if "true"
        """
        self.stdout = stdout
    
    @staticmethod
    def nor_ord(c: str) -> int:
        """Finds the ordinal, 0-indexed value of a given character
        in the Norwegian alphabet

        Args:
            c (str): Character to find the ordinality of

        Returns:
            int: Ordinal value of "c"
        """
        match ord(c):
            case 230: # Æ
                alphabet_ordinal = 26
            case 248: # Ø
                alphabet_ordinal = 27
            case 229: # Å
                alphabet_ordinal = 28
            case _:
                alphabet_ordinal = ord(c) - ord('a')
        return alphabet_ordinal

    def sorted_anagram(self, words: List[str]) -> List[List[str]]:
        """Finds and groups anagrams from a list of words. Uses the fact that
        two words are anagrams when their sorted

        Args:
            words (List[str]): Input list of words

        Returns:
            List[List[str]]: List of grouped anagrams
        """
        anagrams: DefaultDict[str, list] = defaultdict(list)
        for word in words:
            s_word = "".join(sorted(word.lower()))
            
            if word not in anagrams[s_word]:
                anagrams[s_word].append(word)
        
        result = [anagrams for anagrams in list(anagrams.values())
                if len(anagrams) > 1]
        if self.stdout:
            for s in result:
                print(" ".join(s))
        return result
    
    def count_anagram(self, words: List[str]) -> List[List[str]]:
        """Finds and groups anagrams from a list of words. Uses the fact that
        two words with the same character counts are anagrams

        Args:
            words (List[str]): Input list of words

        Returns:
            List[List[str]]: List of grouped anagrams
        """
        anagrams: DefaultDict[tuple, list] = defaultdict(list)
        for word in words:
            counts = [0] * 29 # Norwegian alphabet
            for c in word.lower():
                counts[Anagram.nor_ord(c)] += 1
            key = tuple(counts)
            if word not in anagrams[key]:
                anagrams[key].append(word)
        
        result = [anagrams for anagrams in list(anagrams.values())
                if len(anagrams) > 1]
        if self.stdout:
            for s in result:
                print(" ".join(s))
        return result
    
    def count_anagram_improved(self, words: List[str]) -> List[List[str]]:
        """Finds and groups anagrams from a list of words. Uses the fact that
        two words with the same character counts are anagrams.
        In contrast to "count_anagram()", this method uses the "Counter"
        object to improve performance.

        Args:
            words (List[str]): Input list of words

        Returns:
            List[List[str]]: List of grouped anagrams
        """
        anagrams: DefaultDict[tuple, list] = defaultdict(list)
        for word in words:
            key = tuple(Counter(word.lower()))
            if word not in anagrams[key]:
                anagrams[key].append(word)
        
        result = [anagrams for anagrams in list(anagrams.values())
                if len(anagrams) > 1]
        if self.stdout:
            for s in result:
                print(" ".join(s))
        return result

def read_file_to_list(file_path: str) -> List[str]:
    """Reads a text file into a list, with newlines as a separator
    between list elements

    Args:
        file_path (str): File path to read

    Returns:
        List[str]: List of file contents
    """
    with open(file_path, 'r') as data_file:
        words = [line.rstrip() for line in data_file]
    return words

if __name__ == "__main__":
    file_path = '../datasets/population.txt'
    a = Anagram(stdout = True)
    a.count_anagram_improved(read_file_to_list(file_path))