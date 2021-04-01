#Creating a data set
data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

# del data[0:2]
# print(data)
# del data[14:]
# print(data)

#Setting minimum value.
min_valid = 100
#Setting the maximum value.
max_valid = 200
#Setting a stop value
stop = 0

#Process the low values.
for index, value in enumerate(data):  #This works for sorted lists.
    if value >= min_valid:
        stop = index  #Note that no changes are being made to the list within for loop only in the outter for loop.
        break

print(stop)
del data[:stop] #This works for sorted lists. #Upto, not including.
print(data)

#Getting the high values
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        #Want to keep last item.  
        start = index + 1
        break

del data[start:]
print(data)
