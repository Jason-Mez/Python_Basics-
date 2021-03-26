#Grouping your charecters with Parenthesis.

#Always import regular expression module.
import re

#Using regular exressions with parenhesis as well.
phone_number = re.compile(r"(\d\d)-(\d\d\d\d)")
my_number = phone_number.search("My number is 75-1234 ")
print(f"Hi did you find my number {my_number.group()} ")

#Getting the result in the 1st group.
print(my_number.group(1))

##Getting the 2nd parenthesis.
print(my_number.group(2))

#Getting what the resutls all in one
print(my_number.groups())
