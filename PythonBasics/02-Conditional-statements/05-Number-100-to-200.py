num = int(input())

result = ""

if num < 100:
    result = "Less than 100"
elif 100 <= num <= 200:
    result = "Between 100 and 200"
elif num > 200:
    result = "Greater than 200"

print(result)