import sys
max_num = -sys.maxsize

cmd = input()

while cmd != "Stop":
    num = int(cmd)

    if num > max_num:
        max_num = num

    cmd = input()

print(max_num)