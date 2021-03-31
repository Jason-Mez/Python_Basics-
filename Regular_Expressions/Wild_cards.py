#Using the wild card expression.
#Used to import the regualar expression module
#Most of the time the code is written 3 times
import re

#This will get the 1st occurence of a pattern occured.
nonGreedyRegex = re.compile(r"<.*?>") #Always used a raw string
mo = nonGreedyRegex.search("<To serve man> for dinner >")
print(mo.group())

#This will get the 1st occurence of a pattern of string.
nonGreedyRegex = re.compile(r"<.*?>") #Always use a raw string. #Pay attention to how the
mo = nonGreedyRegex.findall(r"<What To serve man> for dinner. >")
print(mo)  #Notice how there are are "<  > >"  #Putting the question mark next to the asterisk will get the 1st occurence of the pattern.

#Non-Greedy method
#Selecting the pattern
nonGreedyRegex = re.compile(r"<.*?>") #Dot asteriks means that anything can go inside the folder.
#Viewing if the pattern you created is inside the file.
mo = nonGreedyRegex.search("<What to serve a man> for dinner >")
print(mo.group()) #The output still remains the same.
#This is the non-greedy way, non greedy way will use a question at the end of the expression.

print("*" * 100)
print("*" * 100)
print("Now you will see the greedy method in action".center(70))
print("This method does not a ? at th end of the .*".center(70))
print("*" * 100)
print("*" * 100)
print(" ")

#Using the previous example without the .*?
greedyRegex = re.compile(r"<.*>")
GreedyPattern = greedyRegex.search("<What to serve a man> for dinner >")
print(GreedyPattern.group())

#Creating our greedy Pattern
greedyRegex = re.compile(r"<.*>")
GreedyPattern = greedyRegex.search("<What to serve a man > for dinner>")
print(GreedyPattern.group()) #Remember that using search, you need to create .group method. #When calling a method

greedyRegex = re.compile(r"<.*>")
GreedyPattern = greedyRegex.search("<What to serve a man> for dinner > ")
print(GreedyPattern.group())
