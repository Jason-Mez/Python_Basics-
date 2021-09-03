#Working with strings
#Use quotes to create a string.

#Using double quotes, need to stick to using one
print("Cat")

#Using single quotes, need to stick to using one
print('Dog')

#Sometimes it's better to use double quotes instead of single quotes
print("Say hi to bob's, and Bob's is my fav for me")

#But you can use an escape char, of you want to used single quotes only
print('i\'ll show you that we can create a lot of stuff here.')

#Then to use a backslash, you can use a double \\.
print("Am print a back slash, the code actuall used \'\\\\\' to print a single backslash \\")

#Now, i want to multiple lines of code on a single line
print("Looks like\nA new line\nAfter everytime single time\nA Sentence had one more word")

#Raw strings
#Basically taking a string as it is, this will not take any escape charecter into account.
print(r'This is a raw string \n \t \\, escape charecters do not have meaning here.' + "\n")

#Multiline Comments, triple quotes are used to create strings that will span multiple lines
print("""Dear Alice 

Eve's cat is doing well. 

Please do not hesistace to contact me if there are any issues at all. """)
