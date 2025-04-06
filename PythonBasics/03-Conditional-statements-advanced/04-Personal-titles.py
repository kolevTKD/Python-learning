age = float(input())
gender = input()
personal_title = ''

if gender == 'm':
    if age >= 16:
        personal_title = "Mr."
    elif age < 16:
        personal_title = "Master"

elif gender == 'f':
    if age >= 16:
        personal_title = "Ms."
    elif age < 16:
        personal_title = "Miss"

print(personal_title)