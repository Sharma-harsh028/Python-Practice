import math

radius = float(input("Enter radius:"))
height = float(input("Enter height:"))

area = (2 * math.pi * radius * height) + (2 * math.pi * radius**2)
volume = math.pi * radius**2 * height

print("Area:",area)
print("Volume:",volume)