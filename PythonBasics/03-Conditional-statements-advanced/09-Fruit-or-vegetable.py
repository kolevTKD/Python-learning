product_name = input()
product_type = ""

match product_name:
    case "banana" | "apple" | "kiwi" | "cherry" | "lemon" | "grapes":
        product_type = "fruit"
    case "tomato" | "cucumber" | "pepper" | "carrot":
        product_type = "vegetable"
    case _:
        product_type = "unknown"

print(product_type)
