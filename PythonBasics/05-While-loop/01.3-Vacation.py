needed_money = float(input())
available_money = float(input())
spending_streak = 0
days = 0

while available_money < needed_money and spending_streak < 5:

    cmd = input()
    money = float(input())

    if cmd == "save":
        spending_streak = 0
        available_money += money

    elif cmd == "spend":
        spending_streak += 1
        available_money -= money

        if available_money < 0:
            available_money = 0
    days += 1

if spending_streak == 5:
    print("You can't save the money.")
    print(days)

elif available_money >= needed_money:
    print(f"You saved the money for {days} days.")