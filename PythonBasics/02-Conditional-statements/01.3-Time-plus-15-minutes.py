hours = int(input())
minutes = int(input())

time_in_minutes = hours * 60 + minutes
time_plus_15 = time_in_minutes + 15

new_hours = time_plus_15 // 60
new_minutes = time_plus_15 % 60

if new_hours >= 24:
    new_hours -= 24

if new_minutes < 10:
    print(f"{new_hours}:0{new_minutes}")
else:
    print(f"{new_hours}:{new_minutes}")