#!/bin/python3
#https://www.hackerrank.com/challenges/sherlock-and-anagrams
import math
import os
import random
import re
import sys
import string

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):

    substrings = {}
    alphabet = string.ascii_lowercase
    
    for start in range(len(s)):
        for finish in range(start, len(s)):
        
            # init
            substring = [0 for _ in alphabet]
            for letter in s[start:finish+1]:
                substring[ord(letter) - ord(alphabet[0])] += 1

            # tuple is hashable. dict and list aren't
            substring = tuple(substring)
            substrings[substring] = substrings.get(substring, 0) + 1

    res = 0        
    for count in substrings.values():
        res += count * (count-1) // 2
        
    return res

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
