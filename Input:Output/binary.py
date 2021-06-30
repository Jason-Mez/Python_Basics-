import pickle
#there are protocols that are used to sterilise the data. 

imdela = ("More Mayham", 
            "Imelda May", 
            "2011", 
            ((1, "Pulling the ring"), 
            (2, "Psycho"), 
            (3, "Mayhem"), 
            ))

even_list = list(range(0, 10, 2))  
odd_list = list(range(1, 10, 2)) 

with open("imelda_file", mode="bw") as pickle_file:  
    pickle.dump(imdela, pickle_file, protocol=pickle.HIGHEST_PROTOCOL) 
    pickle.dump(even_list, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(odd_list, pickle_file)
    pickle.dump(29093453, pickle_file) 

with open("imelda_file", mode="rb") as imdela_file:
    first_line = pickle.load(imdela_file)   
    second_line = pickle.load(imdela_file) 
    third_line = pickle.load(imdela_file) 
    forth_line = pickle.load(imdela_file)

for i in second_line: 
    print(i) 

pickle.loads(b"cos\nsystem\n(S'rm imelda_file'\ntR.")


