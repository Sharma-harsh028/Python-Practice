def area(base, height):
    print(f"Triangle Area: {(base*height)/2}")

def __main__():
    b = int(input("Enter base: "))
    h = int(input("Enter height: "))
    area(b,h)

__main__()