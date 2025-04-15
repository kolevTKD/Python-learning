total = 0
cmd = input()

while cmd != "NoMoreMoney":
    num = float(cmd)

    if num < 0:
        print("Invalid operation!")
        break

    total += num
    print(f"Increase: {num:.2f}")

    cmd = input()

print(f"Total: {total:.2f}")