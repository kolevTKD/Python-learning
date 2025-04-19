import sys

free_width = int(input())
free_length = int(input())
free_height = int(input())
total_space = free_width * free_length * free_height

cmd = input()

while cmd != "Done":
    packages_count = int(cmd)

    total_space -= packages_count

    if total_space < 0:
        print(f"No more free space! You need {abs(total_space)} Cubic meters more.")
        sys.exit(0)

    cmd = input()

print(f"{total_space} Cubic meters left.")