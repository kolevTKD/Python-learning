import math

wr_seconds = float(input())
dist_meters = float(input())
secs_per_meter = float(input())

resistance_slowing = math.floor(dist_meters // 15) * 12.5
contender_time = dist_meters * secs_per_meter + resistance_slowing

if contender_time >= wr_seconds:
    print(f"No, he failed! He was {contender_time - wr_seconds:.2f} seconds slower.")

else:
    print(f"Yes, he succeeded! The new world record is {contender_time:.2f} seconds.")