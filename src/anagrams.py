from collections import defaultdict, Counter
from typing import List, DefaultDict


class SolveAnagram:
    """The class holds all algorithmic implementations of solving the
    anagram problem, as well as helper methods
    """

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
            case 230:  # Æ
                alphabet_ordinal = 26
            case 248:  # Ø
                alphabet_ordinal = 27
            case 229:  # Å
                alphabet_ordinal = 28
            case _:
                alphabet_ordinal = ord(c) - ord("a")
        return alphabet_ordinal

    @staticmethod
    def sorted_anagram(words: List[str]) -> List[List[str]]:
        """Finds and groups anagrams from a list of words. Uses the fact that
        two words are anagrams if they are equal when sorted

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

        result = [anagrams for anagrams in list(anagrams.values()) if len(anagrams) > 1]

        return result

        """ Big-O analysis of sorted_anagram()
        N is the number of words and S is the size of the longest string
        
        Time complexity  = O(N S log(S))
        Space complexity = O(N S)
        
        The program does one pass over all the words, yielding a time complexity
        of O(N), and for every entry we sort the string. 
        sorted() uses Timsort, which has a worst-case time complexity of O(S log(S))
        We also lookup in the dictionary, which is O(1)
        In the end we also make one final pass over the dictionary, which has
        O(N) time complexity.
        The final time complexity is: O(N S log(S)) + O(N) = O(N S log(S))
        
        The worst-case space complexity is O(N S), because the algorithm
        stores all the strings in the dictionary
        """

    @staticmethod
    def count_anagram(words: List[str]) -> List[List[str]]:
        """Finds and groups anagrams from a list of words. Uses the fact that
        two words with the same character counts are anagrams

        Args:
            words (List[str]): Input list of words

        Returns:
            List[List[str]]: List of grouped anagrams
        """
        anagrams: DefaultDict[tuple, list] = defaultdict(list)
        for word in words:
            counts = [0] * 29  # Norwegian alphabet
            for c in word.lower():
                ordinal_value = SolveAnagram.nor_ord(c)
                counts[ordinal_value] += 1
            key = tuple(counts)  # Convert to tuple to be hashable
            if word not in anagrams[key]:
                anagrams[key].append(word)

        result = [anagrams for anagrams in list(anagrams.values()) if len(anagrams) > 1]

        return result

        """ Big-O analysis of count_anagram()
        N is the number of words and S is the size of the longest string
        
        Time complexity  = O(N S)
        Space complexity = O(N S)
        
        The program does one pass over all the words, yielding a time complexity
        of O(N), and for every entry we count the character occurences in the word,
        and convert the counts to a tuple, both operations have O(S) time complexity
        The final time complexity is: O(N S) + O(N) = O(N S)
        
        The worst-case space complexity is O(N S), because the algorithm
        stores all the strings in the dictionary
        """

    @staticmethod
    def count_anagram_counter(words: List[str]) -> List[List[str]]:
        """Finds and groups anagrams from a list of words. Uses the fact that
        two words with the same character counts are anagrams.
        In contrast to "count_anagram()", this method uses the "Counter"
        object to improve performance.

        Args:
            words (List[str]): Input list of words

        Returns:
            List[List[str]]: List of grouped anagrams
        """
        anagrams: DefaultDict[frozenset, list] = defaultdict(list)
        for word in words:
            key = frozenset(Counter(word.lower()).items())  # frozenset is hashable
            if word not in anagrams[key]:
                anagrams[key].append(word)

        result = [anagrams for anagrams in list(anagrams.values()) if len(anagrams) > 1]

        return result

        """ Big-O analysis of count_anagram_counter()
        N is the number of words and S is the size of the longest string
        
        Time complexity  = O(N S)
        Space complexity = O(N S)
        
        The program does one pass over all the words, yielding a time complexity
        of O(N), and for every entry Counter() counts the character occurences in
        the word, and convert to a frozenset(), both with O(S) time complexity
        The final time complexity is: O(N S) + O(N) = O(N S)
        
        The worst-case space complexity is O(N S), because the algorithm
        stores all the strings in the dictionary
        """


def read_file_to_list(file_path: str) -> List[str]:
    """Reads a text file into a list, with newlines as a separator
    between list elements

    Args:
        file_path (str): File path to read

    Returns:
        List[str]: List of file contents
    """
    with open(file_path, "r") as data_file:
        words = [line.rstrip() for line in data_file]
    return words


if __name__ == "__main__":
    file_path = "../datasets/population.txt"
    data = read_file_to_list(file_path)

    result = SolveAnagram.sorted_anagram(data)
    # result = SolveAnagram.count_anagram(data)
    # result = SolveAnagram.count_anagram_counter(data)

    for s in result:
        print(" ".join(s))
