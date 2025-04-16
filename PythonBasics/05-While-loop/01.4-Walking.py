steps_made = 0

while steps_made < 10000:
    cmd = input()

    if cmd == "Going home":
        steps = int(input())
        steps_made += steps
        break

    steps = int(cmd)
    steps_made += steps

if steps_made >= 10000:
    print("Goal reached! Good job!")
    print(f"{steps_made - 10000} steps over the goal!")
else:
    print(f"{10000 - steps_made} more steps to reach goal.")
