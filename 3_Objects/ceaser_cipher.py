word = input("Enter 3 letter word:")
shift = int(input("shift by how many letters? "))
sm = chr(ord(word[0]) + shift) + chr(ord(word[1]) + shift) + chr(ord(word[2]) + shift)

print(sm)