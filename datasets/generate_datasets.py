from string import ascii_lowercase as alphabet
from random import choice, sample
import csv

def generate(n: int):
    input_dataset = []
    solution_dataset = []
    char_start = 2
    char_range = 6
    
    solution_dict = {}
    
    fieldnames = ["input"] + list(map(
        str,range(1, char_start + char_range + 1)))
    with open(f"dataset_{n}.csv", mode='w') as dataset_csv:
        writer = csv.DictWriter(dataset_csv, fieldnames=fieldnames)
        
        for i in range(0, n//2):
            string_length = choice(range(char_start, char_start + char_range//2))
            gen_string = make_string(string_length)
            anagram_string = ''.join(sample(gen_string,len(gen_string)))
            writer.writerow({'input': gen_string, 
                             str(string_length): anagram_string})
        for i in range(0, n//2): 
            string_length = choice(range(char_start + char_range//2, char_start + char_range))
            gen_string = make_string(string_length)
            writer.writerow({'input': gen_string})        
    
    
def make_string(string_length: int):
    s = ""
    for i in range(0, string_length):
        s += choice(alphabet)
    return s

generate(10000)