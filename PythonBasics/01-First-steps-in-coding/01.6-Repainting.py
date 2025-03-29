protective_nylon_price_sqm = 1.50
paint_price_per_liter = 14.50
paint_thinner_price_per_liter = 5.00

needed_nylon_sqm = int(input())
needed_paint_liters = int(input())
needed_thinner_liters = int(input())
hours_needed = int(input())

nylon_total = (needed_nylon_sqm + 2) * protective_nylon_price_sqm
paint_total = (needed_paint_liters * 1.1) * paint_price_per_liter
thinner_total = needed_thinner_liters * paint_thinner_price_per_liter

total_for_materials = nylon_total + paint_total + thinner_total + 0.40
total_for_workers = (total_for_materials * 0.3) * hours_needed
total_expenses = total_for_materials + total_for_workers

print(total_expenses)