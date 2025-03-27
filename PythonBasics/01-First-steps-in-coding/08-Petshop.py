dogfood_pack_price = 2.50
catfood_pack_price = 4.00

dogfood_packs_count = int(input())
catfood_packs_count = int(input())

dogfood_total = dogfood_pack_price * dogfood_packs_count
catfood_total = catfood_pack_price * catfood_packs_count
total = dogfood_total + catfood_total

print(f"{total} lv.")