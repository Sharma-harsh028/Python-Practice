n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

for i in range(n1,n2+1):
    if i % 2 == 0:
        print(i, end = " " )
print("\n")
for i in range(n1,n2+1):
    
    if i % 2 != 0:
        print(i, end = " " )