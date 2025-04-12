month = input()
nights = int(input())

studio_cost = 0
apartment_cost = 0
studio_total = 0
apartment_total = 0

if month == "May" or month == "October":
    studio_cost = 50
    studio_total = nights * studio_cost

    apartment_cost = 65
    apartment_total = nights * apartment_cost

    if 7 < nights <= 14:
        studio_total -= studio_total * 0.05

    elif nights > 14:
        studio_total -= studio_total * 0.3

elif month == "June" or month == "September":
    studio_cost = 75.2
    studio_total = nights * studio_cost

    apartment_cost = 68.7
    apartment_total = nights * apartment_cost

    if nights > 14:
        studio_total -= studio_total * 0.2

elif month == "July" or month == "August":
    studio_cost = 76
    studio_total = nights * studio_cost

    apartment_cost = 77
    apartment_total = nights * apartment_cost

if nights > 14:
    apartment_total -= apartment_total * 0.1

print(f"Apartment: {apartment_total:.2f} lv.")
print(f"Studio: {studio_total:.2f} lv.")