#Here is my solution for problem solving based on Number Line Jumps question.
#Link for the question : https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true
#Here is main link of problem solving hackerrank : https://www.hackerrank.com/domains/algorithms

#!/bin/python3

def kangaroo(x1, v1, x2, v2):
    # If the kangaroos have the same jump distance but different start positions, they will never meet.
    if v1 == v2:
        if x1 == x2:
            return "YES"
        else:
            return "NO"
    
    # Calculate the difference in starting positions and jump distances
    diff_x = x2 - x1
    diff_v = v1 - v2
    
    # Check if the difference in positions is divisible by the difference in velocities
    if diff_x % diff_v == 0 and (diff_x / diff_v) >= 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')
    fptr.close()
