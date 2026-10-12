temp = float(input("Enter temperature: "))
unit = input("Enter unit(c or f): ")

if unit == "c":
    new_temp = (temp - 32)*5/9

elif unit == "f":
    new_temp = (temp * 9/5) + 32

else:
    print("Check unit!!!")

print(round(new_temp,2))