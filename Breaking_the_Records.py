
#Here is my solution for problem solving based on Breaking the Records.
#Link for the question : https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true
#Here is main link of problem solving hackerrank : https://www.hackerrank.com/domains/algorithms

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Initialize min and max with the score of the first game
    min_score = max_score = scores[0]
    
    # Counters for record breaks
    min_break_count = 0
    max_break_count = 0
    
    # Iterate through the scores starting from the second game
    for score in scores[1:]:
        # Check for breaking the maximum record
        if score > max_score:
            max_score = score
            max_break_count += 1
        # Check for breaking the minimum record
        elif score < min_score:
            min_score = score
            min_break_count += 1
    
    # Return the result as a list [max_break_count, min_break_count]
    return [max_break_count, min_break_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
