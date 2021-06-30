import csv, pathlib 

daily_temperatures = [ 
    [68, 65, 68, 70, 74, 72], 
    [67, 67, 70, 72, 72, 70], 
    [68, 70, 74, 76, 74, 73]  
    ]

file_path = pathlib.Path("/Users/joshuamezieres/Desktop/CSV_WRITER.csv") 
file = file_path.open(encoding="utf-8", mode= "a") 

writer = csv.writer(file) 

for temp in daily_temperatures: 
    writer.writerow(temp) 

file.close()