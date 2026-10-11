
starting_hour = int(input("Enter starting hour: "))
starting_minute = int(input("Enter starting minute: "))
stopping_hour = int(input("Enter stopping hour: "))
stopping_minute = int(input("Enter stopping minute: "))
rate = float(input("Enter hourly rate: "))

start = starting_hour * 60 + starting_minute
stop = stopping_hour * 60 + stopping_minute

total_minutes = stop - start
working_hours = total_minutes / 60
payment = working_hours * rate

print(f"Worked {starting_hour}:{starting_minute:02d} to {stopping_hour}:{stopping_minute:02d}")
print(f"Total hours: {working_hours:.1f}")
print(f"Payment: ${payment:.2f}")
