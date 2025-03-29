annual_fee = int(input())

sneakers_price = annual_fee - annual_fee * 0.4
equipment_price = sneakers_price - sneakers_price * 0.2
ball_price = equipment_price * 0.25
accessories_price = ball_price * 0.2

total_expenses = annual_fee + sneakers_price + equipment_price + ball_price + accessories_price
print(total_expenses)