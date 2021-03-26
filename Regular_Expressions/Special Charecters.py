#Looking for special charecters.
import re

home_number = re.compile(r"\(\+\d\d\)-\d\d\d\d\d\d\d\d")

my_number = home_number.search("My home number is : (+27)-32704356")
print(my_number.group())


#Creating the regulr expression.
#When compiling always use a raw string.
shoes = re.compile("\$\d\d\.\d\d")
my_fav_shoes = shoes.search("My favorites shoes are $20.34")
print(my_fav_shoes.group())

#Matching Zero or more with star.  
    #It can look for zero to Infinity occurences. 
batRegex = re.compile(r"Bat(wo)*man") 
mo1 = batRegex.search("Batwowowowowowowoman") 
print(mo1.group()) 

#Using the ? is an optional charecter. 
#Always compile with a raw string.  
searching_with_question = re.compile(r"Super(wo)?man")
fav_char = searching_with_question.search("My fav char is Superwoman") 
print(fav_char.group()) 
print() 
my_2nd_fav = searching_with_question.search("My fav char is Superman") 
print(my_2nd_fav.group()) 

#Using Using the plus method. 
#Plus, using the + method to search for patterns that need to occur more than once. 
booky = re.compile(r"bo(oks)+!") 

try: 
    fav_book = booky.search("book are the best")  
    print(fav_book.group) 
except: 
    print("The result you are serching needs to appear at least one") 

fav_book_2 = booky.search("I just love all the books! in the world, cant get enough of them")  
print(f"The we have it, we have found that you love : {fav_book_2.group()}") 

#Matching specific Repetitions with Braces. 
#If you want a specific repeat, you can use curly braces - Along side parentheis 
text_to_search = re.compile(r"(Cococo){3}") 
crazy_much = text_to_search.search("Am in love with theCococoCococoCococo") 
print(crazy_much.group()) 

#What if you want a specific range, and you only want to see that specific range or string of charecters.  
#Doing this will produce the longest possible criteria. 
dsm5 = re.compile(r"(dsm5){1,5}") 
text = dsm5.search("The dsm5dsm5dsm5dsm5 criteria is pretty amazing, it has all the psychology disorders in em.")
print(f"The {text.group()} is one that is used view the list of Psychological disorders.")  

#If you want the shortest pattern matched use the question at the end. 
dsm5 = re.compile(r"(dsm5){1,5}?") #The question mark at the end indicates that you are looking for the shortest method.   
text = dsm5.search("The dsm5dsm5dsm5dsm5 criteria is pretty amazing, it has all the psychology disorders in em.")
print(f"The {text.group()} is one that is used view the list of Psychological disorders.") 
  
