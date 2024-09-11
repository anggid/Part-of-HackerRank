#Here is my solution for problem solving based on diagonal difference question.
#Link for the question : https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
#Here is main link of problem solving hackerrank : https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=warmup

#!/bin/python3

def diagonalDifference(arr):
    n = len(arr)  # Number of rows (and columns)
    
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    for i in range(n):
        primary_diagonal_sum += arr[i][i]  # Elements from the primary diagonal
        secondary_diagonal_sum += arr[i][n - 1 - i]  # Elements from the secondary diagonal
    
    # Calculate absolute difference
    difference = abs(primary_diagonal_sum - secondary_diagonal_sum)
    
    return difference

if __name__ == '__main__':
    import os
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input().strip())
    
    arr = []
    
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    result = diagonalDifference(arr)
    
    fptr.write(str(result) + '\n')
    
    fptr.close()
