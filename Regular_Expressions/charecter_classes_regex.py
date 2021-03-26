import re
#Charecter classes. 

#This is a simple script that aims dealing with charecter classes. 

#Using the \D class that is a Non-Number 0-9 #This searches for spaces as well. 
example_compile = re.compile("\D\D\D\D\D\D") 
example_test = example_compile.search("Yada yada yada") 
print(example_test.group()) 
print("*" * 100) 
print("*" * 100) 

#Using the \w chracter   
charecters = re.compile(r"\w\w\w\w \w\w \w\w\w\w\w") 
finding = charecters.search("This is lavie")  
print(finding.group()) #Returned the whole output. 

#Using the \W, to search for special charecters. 
special_char = re.compile(r"(\W\W\W\W){1,3}?") 
char = special_char.search("Here **** , we have is ****") #Searching for special charecters. 
print(char.group())

#The \s option is used for spaces, new line and tab 
_s_n_t = re.compile(r"\w\w\w\w\w\s\w\w\w\?") 
looking = _s_n_t.search("hello how?") 
print(looking.group())