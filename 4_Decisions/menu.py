ans = input("Enter your choice(Lunch/Dinner): ")

if ans == "lunch" or ans=="Lunch":
    print(f"1: Caesar Salad")
    print(f"2: Soup")
    print(f"3: Burrito")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("You order: Caesar Salad")
    elif choice == 2:
        print("You order: Soup")
    elif choice == 3:
        print("You order: Burrito")
    else:
        print("Enter valid Choice!!!")

elif ans == "dinner" or ans == "Dinner":
    print(f"1: Paneer")
    print(f"2: Vegetable")
    print(f"3: Rice")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("You order: Paneer")
    elif choice == 2:
        print("You order: Vegetable")
    elif choice == 3:
        print("You order: Rice")
    else:
        print("Enter valid Choice!!!")

else:
    print("Enter valid Choice!!!")

