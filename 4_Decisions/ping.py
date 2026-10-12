ping = int(input("Enter ping value: "))
ping_report = ""

if ping < 150:
    ping_report = "Ping is low to average"
elif ping >= 150:
    ping_report = "Too high"
else:
    ping_report = "Invalid"

print(ping_report)