def sum_eo(n, t):   #n,positive number,  -- > t, string 
    listy = [] 
    
    if ( t == "e"): 
        for i in range(1, n): 
            if i % 2 == 0:  
                listy.append(i) 
        return sum(listy)  

    elif (t == "o"): 
        for i in range(1, n): 
            if i % 2 != 0:  
                listy.append(i)
        return sum(listy) 
    else: 
        return -1
            

print(sum_eo(10, "e")) 
print(sum_eo(7, "o"))
