#List are great for containng an ordered sequences
#Dictionaries: Great for keeping values.

allGuests = {
    "Alice": {"apples": 5, "Pretzels": 12},
    "Bob": {"ham sandwiches": 3, "apples": 2},
    "Carol": {"cups": 3, "apples pies": 1}
}

def totalBrought(guest, item):
    numBrought = 0
    for k, v in guest.items(): #iterate both the key and values
        numBrought = numBrought + v.get(item, 0) #Getting the values from the inner list.
    return numBrought


print("Number of things being brought")
print(f"-Apples {totalBrought(allGuests, 'apples')}")

#Know that the value is a dictionary, so we can apply a dictionary methods to it.

