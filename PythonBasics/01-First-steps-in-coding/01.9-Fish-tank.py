tank_length = int(input())
tank_width = int(input())
tank_height = int(input())
used_space_percentage = float(input())

tank_volume_dm = tank_length * tank_width * tank_height
tank_volume_l = tank_volume_dm / 1000
needed_liters = tank_volume_l * (1 - used_space_percentage / 100)

print(needed_liters)