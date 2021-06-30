#Append to the file but the 1st colunm of number should be right justified. 
#   1 times 2 is 2
#   2 times 2 is 4
#   3 times 2 is 6
#   4 times 2 is 8
#   5 times 2 is 10
#   6 times 2 is 12
#   7 times 2 is 14
#   8 times 2 is 16
#   9 times 2 is 18
#  10 times 2 is 20
#  11 times 2 is 22
#  12 times 2 is 24 

listy = [ "1 times 2 is 2",
    "2 times 2 is 4",
    "3 times 2 is 6",
    "4 times 2 is 8",
    "5 times 2 is 10",
    "6 times 2 is 12",
    "7 times 2 is 14",
    "8 times 2 is 16",
    "9 times 2 is 18",
    "10 times 2 is 20",
    "11 times 2 is 22", 
    "12 times 2 is 24" 
 ]

c = 0 
with open("/Users/joshuamezieres/Desktop/Python_Projects/Beginner/Input:Output/sample.txt", encoding="utf-8", mode="a") as file_sample:
    for i in range(9): 
        x = listy[c]  
        print(x[0].rjust(2) + x[1:], file=file_sample)  
        c += 1    
    for y in listy[9:]: 
        print(y,file = file_sample)

