pages_count = int(input())
pages_per_hour = int(input())
days_to_read = int(input())

total_time_for_reading = pages_count // pages_per_hour
reading_hours_per_day = total_time_for_reading // days_to_read

print(reading_hours_per_day)