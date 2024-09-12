#Here is my solution for problem solving based on Apple and Orange question.
#Link for the question : https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true
#Here is main link of problem solving hackerrank : https://www.hackerrank.com/domains/algorithms

#!/bin/python3

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Initialize counters for apples and oranges that fall on the house
    apples_on_house = 0
    oranges_on_house = 0
    
    # Count apples that fall on the house
    for apple in apples:
        apple_position = a + apple
        if s <= apple_position <= t:
            apples_on_house += 1
    
    # Count oranges that fall on the house
    for orange in oranges:
        orange_position = b + orange
        if s <= orange_position <= t:
            oranges_on_house += 1
    
    # Print the results
    print(apples_on_house)
    print(oranges_on_house)

if __name__ == '__main__':
    # Reading input
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    # Call the function with the provided input
    countApplesAndOranges(s, t, a, b, apples, oranges)
