def days_alive(years):
    number = round(years * 365.24)
    return number





def __main__():
    years = int(input("ENter number of years: "))
    number = days_alive(years)
    print(f"You have been alive about {number} days.")

__main__()