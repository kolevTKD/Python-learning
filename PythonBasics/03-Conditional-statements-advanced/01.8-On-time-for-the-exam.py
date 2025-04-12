import sys
import math

exam_hour = int(input())
exam_mins = int(input())
arrival_hour = int(input())
arrival_mins = int(input())

arrival = ""
message = ""

exam_time_mins = exam_hour * 60 + exam_mins
arrival_time_mins = arrival_hour * 60 + arrival_mins
hours_diff = abs((exam_time_mins - arrival_time_mins)) // 60
mins_diff = abs((exam_time_mins - arrival_time_mins)) % 60

diff = exam_time_mins - arrival_time_mins

if arrival_time_mins == exam_time_mins:
    print("On time")
    sys.exit(0)

if diff > 0:
    arrival = "On time"
    message = f"{mins_diff} minutes before the start"

    if diff <= 30:
        arrival = "On time"
        message = f"{mins_diff} minutes before the start"

    else:
        arrival = "Early"

        if hours_diff == 0:
            message = f"{mins_diff} minutes before the start"

        else:
            message = f"{hours_diff}:{mins_diff:02} hours before the start"

elif diff < 0:
    arrival = "Late"

    if hours_diff == 0:
        message = f"{mins_diff} minutes after the start"

    else:
        message = f"{hours_diff}:{mins_diff:02} hours after the start"

print(arrival)
print(message)