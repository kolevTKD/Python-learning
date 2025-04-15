import sys

min_num = sys.maxsize

cmd = input()

while cmd != "Stop":
    num = int(cmd)

    if num < min_num:
        min_num = num

    cmd = input()

print(min_num)