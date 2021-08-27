import random
#A short program that counts the number of occurences of each letter in a string.

message = "It was a bright cold day in April, and the clocks were striking."
count = {}

for char in message:
    count.setdefault(char, 0)
    count[char] = count[char] + 1

print(count)

#Hitman or killmonger
my_choice = []
for i in range(10):
    my_choice.append(random.choice(["Killmonger", "Hitman"]))

print(my_choice)

