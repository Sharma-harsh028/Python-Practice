def battle_royale():
    players = int(input("Enter number of players: "))
    find_teammates(players)

def find_teammates(n):
    if n == 3:
        print("Match Starting...")
    elif n < 3:
        print(f"Finding {3-n} players...")
        print("Match Starting...")
    else:
        print("Number of players exceed!!!")

def practiice():
    map1 = input("Enter map: ")
    print(f"Launching practice on {map1} ")


def __main__():
    choice = input("Enter your choice(br/p: )")
    if choice == "br":
        battle_royale()
    elif choice == "p":
        practiice()


__main__()