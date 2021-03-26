#!/usr/bin/env python3 
#creating more special charecters. 
import re 

special_char = re.compile(r"[A-Z0-9]")  
special_char_search = special_char.findall("Hello how are you DOING today 090909 !!!! ")  
print(special_char_search)
