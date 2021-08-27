#Exomple of a dict

myCat = {"Size": "fat",
         "color": "gray",
         "disposition": "loud"
         }

#Accessing a single value
print(myCat["Size"])

#Using a value is string
print(f"My cat has {myCat['color']} fur ")

#Dictionatries Vs Lists
#_> Items in dict are unordered

#Look at the difference between a Dictionary and a list
spam = ["cats", "dogs", "moose"]
bacon = ["moose", "dogs", "cats"]
print(spam == bacon) #Both list have same values
                        #Have different order.
                        #Lists are ordered.

#Looking at the order in a dictionary
eggs = {"name": "Zophie",
        "Species": "cat",
        "age": 8
        }

ham = {"age": 8,
        "Species": "cat",
        "name": "Zophie",
        }
print(eggs == ham) #Same values , but different order.

#Dictionaries cannot be sliced.
try:
    print(eggs[0])
except KeyError:
    print("You cannot slice a key, this has resulted in a key error")

