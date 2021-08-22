#Using random module.
import random

pets = ["Dogs", "Cat", "Moose"]

x = random.choice(pets)

print("Can you gusess which pets are on the above list ? ")

if x == input("Please guess which animal : "):
    print("You are right, well done.")
else:
    print(f"Wrong choice.\nThe correct answer is:  {x}.\n")

random.shuffle(pets)
