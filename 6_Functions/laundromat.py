def laundromat_info():
    print("Liam's Laundry")
    print("7a - 11p")
    washers_open()
    dryers_open()


def washers_open():
    n = int(input("Enter number of washers:"))
    print("Washer Count:",n)

def dryers_open():
    n = int(input("Enter number of dryers:"))
    print("Dryers Count:",n)

laundromat_info()