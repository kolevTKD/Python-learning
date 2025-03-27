time_per_project = 3

name = input()
projects_count = int(input())

total_time = time_per_project * projects_count

print(f"The architect {name} will need {total_time} hours to complete {projects_count} project/s.")
