import re

#Just be aware of the space.
#After the pipe always put a space.
heroRegex = re.compile(r"Batman |Tina Fey")
mo1 = heroRegex.search("Batman and Tina Fey")
print(mo1.group())

mo2 = heroRegex.search("Tina Fey and Batman")
print(mo2.group())

#Use pipe to match several specifications
batRegex = re.compile(r"Bat(man|mobile|copter|bat)")

#Remeber that using the pipe charecter will only return the 1st case or 1st instance.
mo = batRegex.search("Batcopter is the best vehichle, nah.... wait actually the Batmobile is the best one")
print(mo.group(1))
