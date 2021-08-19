#When your Python Progams crashes, the whole program crashes.
#Sometime you do not want the program to crash.
#Want to program to detect errors.

def spam(divideby: int):
    return 42 / divideby

print(spam(2))
print(spam(12))
#print(spam(0)) #THis will cause your program to crash. ds
print(spam(1))

#Error statements can be handled with try and except statments.
def spam(divideby: int):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        return("Error: Invalid argument")

print(spam(0))