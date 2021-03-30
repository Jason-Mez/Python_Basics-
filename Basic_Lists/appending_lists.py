avaliable_parts = [
                    "computer",  
                    "monitor", 
                    "keyboard", 
                    "mouse", 
                    "mouse mat", 
                    "HDMI", 
                    "dvd drive"
                    ] 



current_choice = "-"
valid_choices = [] #Empty list 
for (i) in range(1, len(avaliable_parts) + 1): 
      valid_choices.append(str(i)) 

#Creating an empty list
computer_parts = [] 

while current_choice != "0" : 
    if current_choice in valid_choices: 
        index = int(current_choice) - 1 #Help to get the exact location from the avaliable part list.
        chosen_part = avaliable_parts[index]   
        if chosen_part in computer_parts:  
            print(f"Removing {chosen_part}")
            computer_parts.remove(chosen_part) 
        else: 
            print(f"Adding {chosen_part}")
            computer_parts.append(chosen_part) 
        print(f"Your list now contains: {computer_parts}")
    else: 
        print("Please add options from the list below.\n") 
        for number, part in enumerate(avaliable_parts): 
            print(f"{number + 1} {part}")
     
    current_choice = input() 


print(computer_parts) 







