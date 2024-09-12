#Here is my solution for problem solving based on Between Two Sets question.
#Link for the question : https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true
#Here is main link of problem solving hackerrank : https://www.hackerrank.com/domains/algorithms

#!/bin/python3

def getTotalX(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def lcm(x, y):
        return x * y // gcd(x, y)

    # Find the maximum of array a and minimum of array b
    max_a = max(a)
    min_b = min(b)

    # Generate numbers that are multiples of max_a and check if they are factors of min_b
    count = 0
    for num in range(max_a, min_b + 1, max_a):
        if all(num % k == 0 for k in a) and all(l % num == 0 for l in b):
            count += 1
    
    return count

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    fptr.write(str(total) + '\n')
    fptr.close()
