age = int(input())
washing_machine_cost = float(input())
toy_price = int(input())

total = 0

for i in range (1, age + 1):
    if i % 2 == 0:
        total += 10 * i / 2 - 1
    else:
        total += toy_price

diff = abs(total - washing_machine_cost)

if total >= washing_machine_cost:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")