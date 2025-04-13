from math import floor

tournaments_count = int(input())
initial_pts = int(input())
total_pts = 0
wins = 0

for i in range(0, tournaments_count):
    rank = input()

    if rank == "W":
        total_pts += 2000
        wins += 1
    elif rank == "F":
        total_pts += 1200
    elif rank == "SF":
        total_pts += 720

avg_pts = floor((total_pts // tournaments_count))
total_pts += initial_pts
win_pct = wins / tournaments_count * 100

print(f"Final points: {total_pts}")
print(f"Average points: {avg_pts}")
print(f"{win_pct:.2f}%")
