n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
sum = 0

while n1<n2:
    if n1%2 != 0:
        sum += n1
    n1 = n1 + 2

print(sum)