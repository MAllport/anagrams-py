# anagrams-py

A program that finds anagrams given an input file of words, with tests to check for correctness and efficiency
There are three implemented algorithms to solve anagrams - they can be changed in runner() in test.py if running tests, or in the bottom of the anagrams.py file if running directly
Tests can be run from inside test/ with `python3 -m unittest`
Requires Python 3.10 or newer


Running times of different implementations given a dataset
|                          | _population\_10000000.txt_ | _100000x\_chars\_population.txt_ |
|:------------------------:|:--------------------------:|:--------------------------------:|
|     _sorted\_anagram_    |           4.1071s          |              4.1963s             |
|     _count\_anagram_     |          15.7923s          |              18.2473             |
| _count\_anagram_counter_ |          14.9875s          |              2.7952              |