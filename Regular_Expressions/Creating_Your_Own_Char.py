#Creating you own charecter classes. 
#Sometimes using the standard is not convients to you can use 
import re  

vowelregex = re.compile(r"[aeiouAEIOU]") 
print("--".join(vowelregex.findall("Hello , I GUESS we ARE LoOking for vowelS"))) #This will print every single vowel that we are looking for. 
#reme that findall is used to create a list. 

