# catsNames = []
# while True:
#     print((f"Enter the name of cat + {str(len(catsNames)+ 1)}") + "( or enter nothing to stop)")
#     name = input()
#     if name == "":
#         break
#     catsNames = catsNames + [name]
#     print(catsNames)
#     print("The names are: ")
#     for name in catsNames:
#         print(name)


#A very common common techique in Python, to use the range(len(some_list)).
supplies = ["pens", "staplers", "flamethrowers", "binders"]

try:
    for i in len(supplies):
        print(i)
except TypeError:
    print("An integer is not an iterable object")
    print("This will help to iterate over all indexes in the list.")


for i in range(len(supplies)):
    print(f"The the {supplies[i]} is in {i} place")

for num, i in enumerate(supplies):
    print(f"{num}: {i}")
else:
    print("\n")

