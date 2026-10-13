def t_and_c():
    print("Do you accept terms and conditions?(Y/N)")
    ans = input("Enter answer: ")
    if ans == "Y":
        print("Thank you for accepting.")
    else:
        print("Have a good day.")




while True:
    user = input("User Name ")
    t_and_c()
