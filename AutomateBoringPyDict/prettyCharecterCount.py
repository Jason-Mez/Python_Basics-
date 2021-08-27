import pprint

#A short program that counts the number of occurences of each letter in a string.

message = "It was a bright cold day in April, and the clocks were striking."
count = {}

for char in message:
    count.setdefault(char, 0)
    count[char] = count[char] + 1

print(pprint.pprint(count))
print()