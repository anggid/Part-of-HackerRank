# here is a code for solve string anagram in certify page in Hacker Rank.
# here is a link for get the certify : https://www.hackerrank.com/skills-verification

#!/bin/python3

import math
import os
import random
import re
import sys



def minTime(files, numCores, limit):
    x = []
    y = []
    for f in files:
        if f % numCores == 0:
            x.append(f)
        else:
            y.append(f)
    x.sort(reverse=True)
    return (sum(x[:limit]) // numCores) + sum(x[limit:]) + sum(y)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    files_count = int(input().strip())

    files = []

    for _ in range(files_count):
        files_item = int(input().strip())
        files.append(files_item)

    numCores = int(input().strip())

    limit = int(input().strip())

    result = minTime(files, numCores, limit)

    fptr.write(str(result) + '\n')

    fptr.close()
