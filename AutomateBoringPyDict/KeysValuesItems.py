#Keys, Values, Items

spam = {"color": "red",
        "age": 42
        }

#There are 3 methods used to return keys, values or both.
print("The following values in the spam list are: ")
for value in spam.values():
    print(f"\t***{value}***")

#Printing Both items- values and keys
print("Both key and value")
for key, values in spam.items():
    print(f"The Key is:\t{key}")
    print(f"The item is:\t{values}")
print()
#You can use .keys() to only get the keys.
print("Only the keys")
for key in spam.keys():
    print(key)
print()
#Using "get", you can used the .get method to check if a value exits or not.
picnicItems = {"apples": 5,
               "cups": 2}

print(f"I will bring {picnicItems.get('apples', 0)} apples to the party")
print(f"I will bring {picnicItems.get('eggs', 0)} eggs to the party")

#Setdefault()
spam = {"name": "Pooka",
        "age": 5
        }
spam.setdefault("color", "black")
print(spam)