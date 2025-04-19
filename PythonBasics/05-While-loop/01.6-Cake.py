import sys

width = int(input())
length = int(input())
cake_area = width * length
cmd = input()

while cmd != "STOP":
    pieces = int(cmd)

    cake_area -= pieces

    if cake_area < 0:
        print(f"No more cake left! You need {abs(cake_area)} pieces more.")
        sys.exit(0)

    cmd = input()

print(f"{cake_area} pieces are left.")