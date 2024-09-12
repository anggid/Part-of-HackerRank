#Here is my solution for problem solving based on Mini-Max Sum question.
#Link for the question : https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true
#Here is main link of problem solving hackerrank : https://www.hackerrank.com/domains/algorithms

#!/bin/python3

def miniMaxSum(arr):
    # Calculate the total sum of all elements
    total_sum = sum(arr)
    
    # Initialize minimum and maximum sums with appropriate values
    min_sum = float('inf')
    max_sum = float('-inf')
    
    # Iterate through each element to calculate the sums excluding one element
    for num in arr:
        current_sum = total_sum - num
        if current_sum < min_sum:
            min_sum = current_sum
        if current_sum > max_sum:
            max_sum = current_sum
    
    # Print the results
    print(min_sum, max_sum)

if __name__ == '__main__':
    # Read the input
    arr = list(map(int, input().rstrip().split()))
    
    # Call the function with the input
    miniMaxSum(arr)
