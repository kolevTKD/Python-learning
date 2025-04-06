budget = float(input())
extras_count = int(input())
clothing_price = float(input())

decoration_cost = budget * 0.1
clothing_cost = extras_count * clothing_price

if extras_count > 150:
    clothing_cost -= clothing_cost * 0.1

movie_total = decoration_cost + clothing_cost

if budget >= movie_total:
    print(f"Action!\nWingard starts filming with {budget - movie_total:.2f} leva left.")

else:
    print(f"Not enough money!\nWingard needs {movie_total - budget:.2f} leva more.")