import sys

min_num = sys.maxsize
max_num = -sys.maxsize

nums_count = int(input())

for i in range (0, nums_count):
    num = int(input())

    if num > max_num:
        max_num = num

    if num < min_num:
        min_num = num

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")