import random
import sys

print("*" * 50 )
print("Welcome to the funky name club.")
print("Just a random name generator.")


first = ("Daddy_J", "Sandy", "Crabs")
last = ("Apple_yard", "Chewbaba", "lover", "Soupy_nouply")

while True:
    first_name = random.choice(first)
    last_name = random.choice(last)
    print("\n\n")
    print(f"{first_name} {last_name}")
    print("\n\n")

    try_again = input("Would you like another nick name ?, Press N to exit ")
    if try_again == "N":
        print("Program has been exited")
        sys.exit()
    else:
        print("\n")
        continue


