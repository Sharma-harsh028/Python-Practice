import conversion_module

speed = float(input("How fast were you driving? "))
print(f"Woah! that's like {conversion_module.km2mi(speed)} mph!")
temp = float(input("what was the temperature? "))
print(f"That's like {conversion_module.cel2fah(temp)} degrees Fahrenheit!")
