chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15
delivery = 2.50

chicken_menus_qty = int(input())
fish_menus_qty = int(input())
vegetarian_menus_qty = int(input())

chicken_menus_total = chicken_menus_qty * chicken_menu_price
fish_menus_total = fish_menus_qty * fish_menu_price
vegetarian_menus_total = vegetarian_menus_qty * vegetarian_menu_price

subtotal = chicken_menus_total + fish_menus_total + vegetarian_menus_total
dessert_price = subtotal * 0.2

total = subtotal + dessert_price + delivery
print(total)