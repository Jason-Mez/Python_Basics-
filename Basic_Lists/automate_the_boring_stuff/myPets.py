# myPets = ["Zophie", "Pooka", "Fat-Tail"]
# print("Enter Pets Name")
# #name = input()
#
# if name not in myPets:
#     print(f"I do not have a pet named {name}")
# else:
#     print(f"{name},I have that pet name as well. " )


print("Looking the multple assignment trick")
print("Basically Tuple Unpacking.")

cat = ["fat", "gray", "loud"]

size, color, disposition = cat

try:
    size, color, disposition, name = cat
except ValueError:
    print("Not enough values to unpack")

