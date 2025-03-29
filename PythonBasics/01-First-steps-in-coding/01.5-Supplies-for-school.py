pen_pack_price = 5.80
marker_pack_price = 7.20
detergent_liter_price = 1.20

pen_packs_count = int(input())
marker_packs_count = int(input())
detergent_qty = int(input())
discount_percentage = int(input())

pens_total = pen_packs_count * pen_pack_price
markers_total = marker_packs_count * marker_pack_price
detergent_total = detergent_qty * detergent_liter_price

total = pens_total + markers_total + detergent_total

total_with_discount = total - total * (discount_percentage / 100)

print(total_with_discount)