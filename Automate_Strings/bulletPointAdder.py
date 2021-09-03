#!Python 3
#bulletPointAdder.py - Adds Wikipedia bullets tp the starts
#of each line of text on the clip board

import pyperclip
text = "List of what we want\nThis we need"

#TODO: Seperate Lines and add stars
lines = text.split("\n") #This create a lists.
for i  in range(len(lines)): #Loop through all indexes in hte "lines"
    lines[i] ="*" + lines[i] #add star to each string in the "lines" list


text = "\n".join(lines)
print(text)
