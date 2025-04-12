nums_count = int(input())

left_sum = 0
right_sum = 0

for i in range (0, nums_count * 2):
    num = int(input())

    if i < nums_count:
        left_sum += num

    elif i >= nums_count:
        right_sum += num

diff = abs(left_sum - right_sum)

if diff == 0:
    print(f"Yes, sum = {left_sum}")

else:
    print(f"No, diff = {diff}")