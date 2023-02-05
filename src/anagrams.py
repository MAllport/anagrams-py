from collections import defaultdict, Counter

class Anagram:
    def __init__(self, test_caller):
        self.test_caller = test_caller
    
    @staticmethod
    def nor_ord(c: chr):
        match ord(c):
            case 230: # Æ
                alphabet_chr = 26
            case 248: # Ø
                alphabet_chr = 27
            case 229: # Å
                alphabet_chr = 28
            case _:
                alphabet_chr = ord(c) - ord('a')
        return alphabet_chr

    def naive_anagram(self, words: list[str]):
        anagrams = defaultdict(list)
        for word in words:
            s_word = "".join(sorted(word.lower()))
            
            if word not in anagrams[s_word]:
                anagrams[s_word].append(word)
        
        result = [anagrams for anagrams in list(anagrams.values())
                if len(anagrams) > 1]
        if not self.test_caller:
            for s in result:
                print(" ".join(s))
        return result
    
    def count_anagram(self, words: list[str]):
        anagrams = defaultdict(list)
        for word in words:
            counts = [0] * 29 # Norwegian alphabet
            for c in word.lower():
                counts[Anagram.nor_ord(c)] += 1
            key = tuple(counts)
            if word not in anagrams[key]:
                anagrams[key].append(word)
        
        result = [anagrams for anagrams in list(anagrams.values())
                if len(anagrams) > 1]
        if not self.test_caller:
            for s in result:
                print(" ".join(s))
        return result
    
    def count_anagram_improved(self, words: list[str]):
        anagrams = defaultdict(list)
        for word in words:
            key = tuple(Counter(word))
            if word not in anagrams[key]:
                anagrams[key].append(word)
        
        result = [anagrams for anagrams in list(anagrams.values())
                if len(anagrams) > 1]
        if not self.test_caller:
            for s in result:
                print(" ".join(s))
        return result

def read_file_to_list(file_path):
    with open(file_path, 'r') as data_file:
        words = [line.rstrip() for line in data_file]
    return words

if __name__ == "__main__":
    file_path = '../datasets/100x_chars_population_100000.txt'
    a = Anagram(test_caller = False)
    a.naive_anagram(read_file_to_list(file_path))