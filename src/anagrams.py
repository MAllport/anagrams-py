def naive_anagram(words: list[str]):
    anagrams = {}
    for word in words:
        s_word = "".join(sorted(word))
        if s_word not in anagrams:
            anagrams[s_word] = [word]
        else:
            anagrams[s_word].append(word)
    return [anagrams for anagrams in list(anagrams.values())
            if len(anagrams) > 1]

def naive_anagram_case_sensitive_unique(words: list[str]):
    anagrams = {}
    for word in words:
        s_word = "".join(sorted(word.lower()))
        if s_word in anagrams and word not in anagrams[s_word]:
            anagrams[s_word].append(word)
        else:
            anagrams[s_word] = [word]
    for s in [anagrams for anagrams in list(anagrams.values())
            if len(anagrams) > 1]:
        print(" ".join(s))

def read_file_to_list():
    file_path = '../datasets/population.txt'
    with open(file_path, 'r') as data_file:
        words = [line.rstrip() for line in data_file]
    return words
    
naive_anagram_case_sensitive_unique(read_file_to_list())