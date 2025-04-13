import sys

max_num = -sys.maxsize

nums_count = int(input())
sum_nums = 0

for i in range(0, nums_count):
    num = int(input())

    if num > max_num:
        max_num = num

    sum_nums += num

diff = abs(max_num - (sum_nums - max_num))

if max_num == sum_nums - max_num:
    print("Yes")
    print(f"Sum = {max_num}")

else:
    print("No")
    print(f"Diff = {diff}")