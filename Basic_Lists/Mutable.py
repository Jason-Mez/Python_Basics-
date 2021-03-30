#Mutable object is ones value that can be changed. 
#Examples of mutable objects are : 
    #Lists 
    #dict
    #set 
    #ByteArray 

#Shopping_List: 
shopping_list = [ "Milk", 
                "Cookie", 
                "Cream", 
                "Baking Soda", 
                "Sugar" 
                ]  

another_list = shopping_list  
print(id(shopping_list)) 
print(id(another_list)) 

#adding another item to our list. 
shopping_list += ["flour"] 
print(id(shopping_list)) 
#Note hat the id stays the same. When you add an item, the contents of the list has changed but a new object was created. 
#The value did not change.  

#chain a list together 
a = b = c = d = e = f = another_list 

print("Now adding almonds to the list") 
b += ["almond"] 
print(c) 
print(d) 
print(e) 
print(f) 
#Notice that all this will have the same ID 