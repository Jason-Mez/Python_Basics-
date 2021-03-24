#Regular Expression is just text matching.

#Importing re, using the re function.
import re

#Using re.compile ---> Shows the pattern you are searching for.
phoneNumRegex =  re.compile(r"\d\d-\d\d-\d\d\d\d")

#Using the .seach function to search through the pattern compiled
mo = phoneNumRegex.search("My number 20-02-1994")

#print to see if we get the match that we want.
print(mo.group())
