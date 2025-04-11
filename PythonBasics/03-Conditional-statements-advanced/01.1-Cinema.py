proj_type = input()
rows = int(input())
cols = int(input())

ticket_price = 0

if proj_type == "Premiere":
    ticket_price = 12.0

elif proj_type == "Normal":
    ticket_price = 7.5

elif proj_type == "Discount":
    ticket_price = 5.0

total = rows * cols * ticket_price

print(f"{total:.2f} leva.")