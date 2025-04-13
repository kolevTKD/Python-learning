import sys

actor_name = input()
academy_pts = float(input())
jury_count = int(input())

total_pts = academy_pts

for i in range (0, jury_count):
    jm_name = input()
    jm_pts = float(input())

    total_pts += (len(jm_name) * jm_pts) / 2

    if total_pts >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_pts:.1f}!")
        sys.exit(0)

print(f"Sorry, {actor_name} you need {1250.5 - total_pts:.1f} more!")