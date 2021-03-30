#Immutablility are bascailly items that cannot be changed. 
#The immutale types are built into Python. 
    #int 
    #float 
    #tuple 
    #bool 
    #string 
#Using the ID functions to test this. 
#Am Id to an object is assinged everytime that is created. 
#An ID objct memomry space will be diffrent everytime you run the project. 

#Basically these are the value that cannot be changed, 

string = "Hello"  
copy_cat = string
print(id(string), id(copy_cat), sep="\n")   #Notice how the IDS are the same. 
 
#Looks like ID are the same if the contents stored within them are the same.  
another_same_string = "Hello" 
print(id(another_same_string))  

#Viewing the ID after concatenating to a new list. 
string += "llo" 
print(id(string)) #Notice how the id has changed. 
