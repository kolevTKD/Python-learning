nums_count = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(0, nums_count):
    num = int(input())

    if num < 200:
        p1 += 1
    elif 200 <= num < 400:
        p2 += 1
    elif 400 <= num < 600:
        p3 += 1
    elif 600 <= num < 800:
        p4 += 1
    elif num >= 800:
        p5 += 1

print(f"{p1 / nums_count * 100:.2f}%")
print(f"{p2 / nums_count * 100:.2f}%")
print(f"{p3 / nums_count * 100:.2f}%")
print(f"{p4 / nums_count * 100:.2f}%")
print(f"{p5 / nums_count * 100:.2f}%")