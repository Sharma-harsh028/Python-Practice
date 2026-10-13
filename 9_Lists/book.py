book_list = ["Pachinko", "A Hitchhiker's Guide to the Galaxy", "Moby Dick", "Beloved", "A Farewell to Arms", "Anna Karenina", "The Golden Notebook"]

new_list = [e for e in book_list if e[0] == "A"]

new_list.sort()
print(new_list)