one_person_cost = 18
apartment_cost = 25
president_ap_cost = 35

days_of_stay = int(input())
room_type = input()
rating = input()

nights = days_of_stay - 1
total = 0

if room_type == "room for one person":
    total = nights * one_person_cost

elif room_type == "apartment":
    total = nights * apartment_cost

    if days_of_stay < 10:
        total -= total * 0.3

    elif 10 <= days_of_stay <= 15:
        total -= total * 0.35

    elif days_of_stay > 15:
        total *= 0.5

elif room_type == "president apartment":
    total = nights * president_ap_cost

    if days_of_stay < 10:
        total -= total * 0.1

    elif 10 <= days_of_stay <= 15:
        total -= total * 0.15

    elif days_of_stay > 15:
        total -= total * 0.2

if rating == "positive":
    total *= 1.25

elif rating == "negative":
    total -= total * 0.1

print(f"{total:.2f}")