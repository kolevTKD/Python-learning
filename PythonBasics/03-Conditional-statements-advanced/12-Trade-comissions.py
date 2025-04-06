city = input()
sales = float(input())
commissions = 0.0
valid_input = True

match city:
	case "Sofia":
		if 0 <= sales <= 500:
			commissions = 0.05
		elif 500 < sales <= 1000:
			commissions = 0.07
		elif 1000 < sales <= 10000:
			commissions = 0.08
		elif 10000 < sales:
			commissions = 0.12
		else:
			print("error")
			valid_input = False

	case "Varna":
		if 0 <= sales <= 500:
			commissions = 0.045
		elif 500 < sales <= 1000:
			commissions = 0.075
		elif 1000 < sales <= 10000:
			commissions = 0.1
		elif 10000 < sales:
			commissions = 0.13
		else:
			print("error")
			valid_input = False

	case "Plovdiv":
		if 0 <= sales <= 500:
			commissions = 0.055
		elif 500 < sales <= 1000:
			commissions = 0.08
		elif 1000 < sales <= 10000:
			commissions = 0.12
		elif 10000 < sales:
			commissions = 0.145
		else:
			print("error")
			valid_input = False

	case _:
		print("error")
		valid_input = False

if valid_input:
	print(f"{sales * commissions:.2f}")