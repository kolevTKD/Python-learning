name = input()
year = 1
total = 0
fails_count = 0
has_failed = False

while year <= 12:
    grade = float(input())

    if grade < 4.0:

        if has_failed:
            print(f"{name} has been excluded at {year} grade")
            break

        has_failed = True
        continue

    total += grade

    if year == 12:
        print(f"{name} graduated. Average grade: {total / year:.2f}")
        break

    year += 1