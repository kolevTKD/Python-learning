puzzle_price = 2.60
doll_price = 3.0
plush_price = 4.10
minion_price = 8.20
toy_tuck_price = 2.0

trip_cost = float(input())
puzzles_count = int(input())
dolls_count = int(input())
plushies_count = int(input())
minions_count = int(input())
toy_trucks_count = int(input())

puzzles_total = puzzles_count * puzzle_price
dolls_total = dolls_count * doll_price
plushies_total = plushies_count * plush_price
minions_total = minions_count * minion_price
toy_trucks_total = toy_trucks_count * toy_tuck_price

total = puzzles_total + dolls_total + plushies_total + minions_total + toy_trucks_total
toys_count = puzzles_count + dolls_count + plushies_count + minions_count + toy_trucks_count

if toys_count >= 50:
    total -= total * 0.25

total -= total * 0.1

if total >= trip_cost:
    print(f"Yes! {total - trip_cost:.2f} lv left.")

else:
    print(f"Not enough money! {trip_cost - total:.2f} lv needed.")