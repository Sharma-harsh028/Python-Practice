list1 = [1,2,3,4,81,23,656,2323,67,323,7,4]
sum = 0

for i in list1:
    if i < 10:
        sum = sum + i
    else:
        continue
print(sum)