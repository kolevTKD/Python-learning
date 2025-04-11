import sys

budget = float(input())
season = input()

if not (season == "summer" or season == "winter"):
    sys.exit(0)

dest = ""
site = ""
spent_money = 0

if budget <= 100:
    dest = "Bulgaria"

    if season == "summer":
        spent_money = budget * 0.3
        site = "Camp"

    elif season == "winter":
        spent_money = budget * 0.7
        site = "Hotel"

elif 100 < budget <= 1000:
    dest = "Balkans"

    if season == "summer":
        spent_money = budget * 0.4
        site = "Camp"

    elif season == "winter":
        spent_money = budget * 0.8
        site = "Hotel"

elif budget > 1000:
    dest = "Europe"
    spent_money = budget * 0.9
    site = "Hotel"

print(f"Somewhere in {dest}")
print(f"{site} - {spent_money:.2f}")
