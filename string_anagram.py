# here is a code for solve string anagram in certify page in Hacker Rank.
# here is a link for get the certify : https://www.hackerrank.com/skills-verification
#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

def stringAnagram(dictionary, query):
    d = defaultdict(int)
    for w in dictionary:
        d["".join(sorted(w))] += 1
    ans = []
    for w in query:
        w = "".join(sorted(w))
        ans.append(d[w] if w in d else 0)
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    dictionary_count = int(input().strip())

    dictionary = []

    for _ in range(dictionary_count):
        dictionary_item = input()
        dictionary.append(dictionary_item)

    query_count = int(input().strip())

    query = []

    for _ in range(query_count):
        query_item = input()
        query.append(query_item)

    result = stringAnagram(dictionary, query)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
