price_per_sqm = 7.61
discount_percentage = 0.18

total_sqm = float(input())

total_price_no_discount = total_sqm * price_per_sqm
discount_sum = total_price_no_discount * discount_percentage
total_price = total_price_no_discount - discount_sum

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount_sum} lv.")