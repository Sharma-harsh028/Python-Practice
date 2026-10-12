n = int(input("Enter numerator: "))
d = int(input("Enter denominator: "))

if d>0:
    print(f"Result: {n/d}")

else:
    print("Denominator cannot be 0. enter again")
    d = int(input("Enter denominator: "))
    print(f"Result: {n/d}")
