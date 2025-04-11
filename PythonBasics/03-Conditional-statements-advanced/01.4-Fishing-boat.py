import sys

budget = int(input())
season = input()
fishermen = int(input())

if not (season == "Spring" or season == "Summer" or season == "Autumn" or season == "Winter"):
    sys.exit(0)

boat_rent = 0

if season == "Spring":
    boat_rent = 3000

elif season == "Summer" or season == "Autumn":
    boat_rent = 4200

elif season == "Winter":
    boat_rent = 2600

total = boat_rent

if fishermen <= 6:
    total *= 1 - 0.1

elif 7 < fishermen <= 11:
    total *= 1 - 0.15

elif fishermen >= 12:
    total *= 1 - 0.25

if fishermen % 2 == 0 and not season == "Autumn":
    total *= 1 - 0.05

if budget >= total:
    print(f"Yes! You have {budget - total:.2f} leva left.")

else:
    print(f"Not enough money! You need {total - budget :.2f} leva.")