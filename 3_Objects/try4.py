str1 = input("enter 1st string: ")
str2 = input("enter 2nd string: ")
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

my_tuple = tuple()

my_tuple = my_tuple + (str1,) + (str2,) + (num1,) + (num2,)
print(my_tuple)