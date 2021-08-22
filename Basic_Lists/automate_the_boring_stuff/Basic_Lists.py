#Lists and Tuples can contain multiple values
#List => ordered sequence.
#List =>[]
#Values in the list are in "items"

spam = ["cat", "bat", "rat", "elephant"]

#Accessing individual elements in a list
#Access items start
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])

#You can access item in a list with ints as well
print(spam[int(1)])
print(spam[int(2)])
print(spam[int(3)])

print(["cat", "bat", "rat", "elephant"][2]) #Accessing a list on the same line it was created.

#You can create a list within a list.
spam_list_2 = [["cat", "bat"], [10,30,50,50]]

#You can get index error cause
#print(spam_list_2[1000])

try:
    print(spam_list_2[1000])
except IndexError:
    print("The item you\'re trying to access is out of bounds")

#Removing values from lists
spam = ["cat", "bat", "rat", "elephant"]
print(f"The length of the spam list is {len(spam)}")

#Using the del statement
del spam[2]
print(spam)
print(f"The length of the spam list is {len(spam)}") #Notice how the Length has decreased., 