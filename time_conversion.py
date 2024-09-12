#Here is my solution for problem solving based on Time Conversion question.
#Link for the question : https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true
#Here is main link of problem solving hackerrank : https://www.hackerrank.com/domains/algorithms

#!/bin/python3

def timeConversion(s):
    # Extract the period (AM/PM)
    period = s[-2:]
    # Extract the time without the period
    time_str = s[:-2]
    
    # Split the time into hours, minutes, and seconds
    hours, minutes, seconds = time_str.split(':')
    
    # Convert hours to integer for processing
    hours = int(hours)
    
    # Convert hours based on AM/PM period
    if period == 'AM':
        if hours == 12:
            hours = 0  # Midnight case
    elif period == 'PM':
        if hours != 12:
            hours += 12  # Convert PM hour to 24-hour format
    
    # Format hours, minutes, and seconds to two digits
    return f'{hours:02}:{minutes}:{seconds}'

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
