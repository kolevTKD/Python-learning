import sys

bad_grades_allowed = int(input())

cmd = input()

bad_grades_count = 0
number_of_problems = 0
grades_sum = 0
last_problem = ""

while cmd != "Enough":
    grade = int(input())

    if grade <= 4:
        bad_grades_count += 1

        if bad_grades_count == bad_grades_allowed:
            print(f"You need a break, {bad_grades_count} poor grades.")
            sys.exit(0)

    number_of_problems += 1
    grades_sum += grade
    last_problem = cmd

    cmd = input()

print(f"Average score: {grades_sum / number_of_problems:.2f}")
print(f"Number of problems: {number_of_problems}")
print(f"Last problem: {last_problem}")