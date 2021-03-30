n = int(input()) 
empty_string = []


for i in range(n):
    row = input() 
    empty_string.append(row) 

    for i in empty_string: 
        if 0 == i: 
            i.replace(0, "-")

print(empty_string)
