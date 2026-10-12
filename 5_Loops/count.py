f = 1
g = 1
count = 0
print(f, end = " ")

while g<20:
    print(g, end=" ")
    temp = f
    f = g
    g = g + temp
    count += 1

print("\nLoop count =",count)