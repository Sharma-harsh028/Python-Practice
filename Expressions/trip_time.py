current_hour = int(input("Enter current hour:"))
current_minute = int(input("Enter current minute:"))

trip_time = int(input("Enter trip time in minutes:"))

arrival_hour = (current_hour + trip_time//60 + (current_minute + trip_time%60)//60)%24
arrival_minute = (current_minute + trip_time%60)%60
print("Arrival hour is", arrival_hour)
print("Arrival minute is",arrival_minute)