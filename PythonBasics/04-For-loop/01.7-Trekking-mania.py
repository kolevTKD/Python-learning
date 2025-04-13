groups_count = int(input())
groups = [0] * 5

total_climbers = 0

for i in range (0, groups_count):

    climbers = int(input())
    total_climbers += climbers

    if climbers <= 5:
        groups[0] += climbers
    elif 6 <= climbers <= 12:
        groups[1] += climbers
    elif 13 <= climbers <= 25:
        groups[2] += climbers
    elif 26 <= climbers <= 40:
        groups[3] += climbers
    elif 41 <= climbers:
        groups[4] += climbers


for ppl in groups:
    print(f"{ppl / total_climbers * 100:.2f}%")