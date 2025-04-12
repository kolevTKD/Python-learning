import sys

num1 = int(input())
num2 = int(input())
operand = input()
result = 0

if operand == "/" or operand == "%":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
        sys.exit(0)

    if operand == "/":
        result = num1 / num2
        print(f"{num1} / {num2} = {result:.2f}")

    elif operand == "%":
        result = num1 % num2
        print(f"{num1} % {num2} = {result:}")

elif operand == "+" or operand == "-" or operand == "*":
    if operand == "+":
        result = num1 + num2

    elif operand == "-":
        result = num1 - num2

    elif operand == "*":
        result = num1 * num2

    if result % 2 == 0:
        print(f"{num1} {operand} {num2} = {result} - even")

    else:
        print(f"{num1} {operand} {num2} = {result} - odd")