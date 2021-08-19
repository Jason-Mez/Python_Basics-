#Scope ---> Container

#What is a Local Scope
#Functions -> Variables assigned within in the function

#Global scope
#Variable that exits outside the scope.

#Variable must be either local or global, cannot be both.

def spam():
    eggs = 31_324

spam()
try:
    print(eggs)
except Exception:
    print("Sorry, you cannot call on local variables in a function.")