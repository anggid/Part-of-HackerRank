#Here is my solution for problem solving based on Grading Students question.
#Link for the question : https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
#Here is main link of problem solving hackerrank : https://www.hackerrank.com/domains/algorithms

#!/bin/python3

def gradingStudents(grades):
    rounded_grades = []
    
    for grade in grades:
        if grade >= 38:
            next_multiple_of_5 = ((grade + 4) // 5) * 5
            if next_multiple_of_5 - grade < 3:
                rounded_grades.append(next_multiple_of_5)
            else:
                rounded_grades.append(grade)
        else:
            rounded_grades.append(grade)
    
    return rounded_grades

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())
    grades = [int(input().strip()) for _ in range(grades_count)]

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)) + '\n')
    fptr.close()
