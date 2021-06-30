#Writing multiple  lines 
lines_write = [ 
    "\nLine_1 \n", 
    "Line_2  \n", 
    "Line_3 \n", 
]  

with open("/Users/joshuamezieres/Desktop/New_File.txt", encoding="utf-8", mode="wa") as read: 
    read.write("Now am appending to a file.")  
    read.writelines(lines_write)   