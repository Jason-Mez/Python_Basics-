menus = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]


#You can delete items by looping through the index and using del 
#You can delete items by looping through the index and using del 
#You can delete itme in a list by looping through the value in the list. 

#This can be accomplished by the range function 
#This can be accomplished by using the range function. 
#This can be accomplished by using the range function. 

for individual_menu in menus:  
    for index in range(len(individual_menu)- 1, -1, -1): 
        if individual_menu[index] == "spam" :
            del individual_menu[index] 
    print(individual_menu) 

for individual_menu in menus:   #Know what you are dealing with string or list, Know what you are dealing with string or list, know what you are dealing with string or list. 
    for item in individual_menu: #Dealing with a list.  
        if item != "spam":  #dealing with a string.  
            print(item) 
    print()                    #Know where to indent , #Know where to indent, #Know where to indent.
