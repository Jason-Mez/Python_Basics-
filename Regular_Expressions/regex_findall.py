#search only looks for the 1st match of a pattern. 
#findall(), return everystring that matches a pattern. 
import re

#Using findall(), instead of search. 
first_one = re.compile(r"\d\d-\d\d-\d\d")    
numbers= first_one.findall("22-44-66, 11-33-55-77") 

