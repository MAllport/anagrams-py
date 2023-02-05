
class Anagram:
    def naive_anagram(self, words: list[str]):
        anagrams = {}
        for word in words:
            s_word = "".join(sorted(word))
            if s_word not in anagrams:
                anagrams[s_word] = [word]
            else:
                anagrams[s_word].append(word)
        result = [anagrams for anagrams in list(anagrams.values())
                if len(anagrams) > 1]
        for s in result:
            print(" ".join(s))
        return result

    def naive_anagram_improved(self, words: list[str]):
        anagrams = {}
        for word in words:
            s_word = "".join(sorted(word.lower()))
            if s_word in anagrams and word not in anagrams[s_word]:
                anagrams[s_word].append(word)
            else:
                anagrams[s_word] = [word]
        result = [anagrams for anagrams in list(anagrams.values())
                if len(anagrams) > 1]
        for s in result:
            print(" ".join(s))
        return result

def read_file_to_list(file_path):
    with open(file_path, 'r') as data_file:
        words = [line.rstrip() for line in data_file]
    return words

if __name__ == "__main__":
    file_path = '../datasets/population.txt'
    a = Anagram()
    a.naive_anagram_case_sensitive_unique(read_file_to_list(file_path))