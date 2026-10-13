sports = ["Basketball", "Football", "tennis", "Table Tennis", "Soccer"]

count = 0
for sport in sports:
    if sport == "Soccer":
        count += 1
        break
if count == 1:
    print("Found")

else:
    print("Not found")