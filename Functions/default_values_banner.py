def banner(text=" ", screen_width= 80): #Do not leave spaces when creating default parameters.  
     
    if len(text) > screen_width - 4 :
        raise ValueError(f"The {text} is larger than the specified width {screen_width}") 

    if text == "*": 
        print("*" * screen_width) 
    else:  
        cetenred_text = text.center(screen_width - 4 )
        output_string = f"**{cetenred_text}**"    
        print(output_string) 


banner(screen_width=80)
