import copy

#Sometimes you may want to create a duplicate list and basically experiment with it.
spam = ["A", "B", "C", "D"]
print(id(spam))
print(spam)
cheese = copy.copy(spam)
print(id(cheese)) #Notice how id's are different.

cheese[1] = 42
print(cheese)
print(id(cheese))

print(cheese)

