nums_count = int(input())

even_sum = 0
odd_sum = 0

for i in range (1, nums_count + 1):
    num = int(input())

    if i % 2 == 0:
        even_sum += num

    else:
        odd_sum += num

diff = abs(even_sum - odd_sum)

if diff == 0:
    print("Yes")
    print(f"Sum = {even_sum}")

else:
    print("No")
    print(f"Diff = {diff}")