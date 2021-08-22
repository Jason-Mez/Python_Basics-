#A method is thing as a function. Except it is called on a value.

#Index methods
spam = ["Hello", "hi", "howdy", "heyas"]
print(spam.index("Hello"))

#Value Error when you try to index something that you feel does not exist.
try:
    spam.index("dklajdsf")
except ValueError:
    print("Sorry, this value is not in the list.")

#Adding values to a list
#2 methods -> append, insert

spam.append("chicken")
spam.insert(2, "Egg")

#Removing values from lists.
#To remove a value from a list.
spam.remove("hi")
spam.sort()