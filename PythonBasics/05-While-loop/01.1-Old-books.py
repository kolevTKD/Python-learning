import sys

book = input()
counter = 0
cmd = input()

while cmd != "No More Books":
    searched = cmd

    if searched == book:
        print(f"You checked {counter} books and found it.")
        sys.exit(0)

    counter += 1
    cmd = input()

print("The book you search is not here!")
print(f"You checked {counter} books.")