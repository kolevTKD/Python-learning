fruit = input()
day_of_week = input()
quantity = float(input())
price = 0.0
valid_input = True

match day_of_week:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        match fruit:
            case "banana":
                price = 2.5
            case "apple":
                price = 1.2
            case "orange":
                price = 0.85
            case "grapefruit":
                price = 1.45
            case "kiwi":
                price = 2.7
            case "pineapple":
                price = 5.5
            case "grapes":
                price = 3.85
            case _:
                print("error")
                valid_input = False

    case "Saturday" | "Sunday":
        match fruit:
            case "banana":
                price = 2.7
            case "apple":
                price = 1.25
            case "orange":
                price = 0.9
            case "grapefruit":
                price = 1.60
            case "kiwi":
                price = 3.0
            case "pineapple":
                price = 5.6
            case "grapes":
                price = 4.2
            case _:
                print("error")
                valid_input = False
    case _:
        print("error")
        valid_input = False

if valid_input:
    print(f"{quantity * price:.2f}")