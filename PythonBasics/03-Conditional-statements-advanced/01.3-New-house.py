import sys

flower_type = input()

if not (flower_type == "Roses" or flower_type == "Dahlias" or flower_type == "Tulips" or flower_type == "Narcissus" or flower_type == "Gladiolus"):
    sys.exit(0)

flowers_count = int(input())
budget = float(input())

flower_price = 0
total = 0

match flower_type:
    case "Roses":
        flower_price = 5
        total = flowers_count * flower_price

        if flowers_count > 80:
            total -= total * 0.1

    case "Dahlias":
        flower_price = 3.8
        total = flowers_count * flower_price


        if flowers_count > 90:
            total -= total * 0.15

    case "Tulips":
        flower_price = 2.8
        total = flowers_count * flower_price

        if flowers_count > 80:
            total -= total * 0.15

    case "Narcissus":
        flower_price = 3
        total = flowers_count * flower_price

        if flowers_count < 120:
            total *= 1.15

    case "Gladiolus":
        flower_price = 2.5
        total = flowers_count * flower_price

        if flowers_count < 80:
            total *= 1.2

if budget >= total:
    print(f"Hey, you have a great garden with {flowers_count} {flower_type} and {budget - total:.2f} leva left.")

else:
    print(f"Not enough money, you need {total - budget:.2f} leva more.")