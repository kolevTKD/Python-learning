deposit_sum = float(input())
deposit_term = int(input())
year_interest_percentage = float(input())

total_interest = deposit_sum * (year_interest_percentage / 100)
monthly_interest = total_interest / 12
total_sum = deposit_sum + deposit_term * monthly_interest

print(total_sum)