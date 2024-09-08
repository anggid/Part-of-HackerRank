#Here is my solution for string manipulation based on Sherlock and the Valid String question.
#Link for the question : https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
#Here is main link of string manipulation hackerrank : https://www.hackerrank.com/interview/interview-preparation-kit/strings/challenges

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    from collections import Counter

    # Step 1: Get frequency of each character
    char_count = Counter(s)
    
    # Step 2: Get the frequencies of these counts
    frequencies = list(char_count.values())
    
    # Step 3: Use a set to get the unique frequencies
    unique_frequencies = set(frequencies)
    
    # If there's only one unique frequency, the string is valid
    if len(unique_frequencies) == 1:
        return "YES"
    
    # If there are more than two unique frequencies, it's not valid
    if len(unique_frequencies) > 2:
        return "NO"
    
    # There are exactly two unique frequencies, let's analyze them
    freq1, freq2 = min(unique_frequencies), max(unique_frequencies)
    
    # Count how often each frequency occurs
    freq_count = Counter(frequencies)
    
    # Case 1: If one frequency is 1 and it appears exactly once, we can remove that character
    if freq1 == 1 and freq_count[freq1] == 1:
        return "YES"
    
    # Case 2: If the higher frequency is just one more than the lower frequency,
    # and it appears exactly once, we can remove one occurrence of the character with the higher frequency
    if freq2 == freq1 + 1 and freq_count[freq2] == 1:
        return "YES"
    
    # In all other cases, it's not valid
    return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
