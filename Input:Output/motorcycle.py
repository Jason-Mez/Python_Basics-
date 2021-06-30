import shelve  
import pickle

with shelve.open("bikies") as bike: 
    bike["Make"] = "Honda" 
    bike["model"] = "250 Dream" 
    bike["color"] = "red" 
    bike["engine_size"] = 250    

    del bike["engine_size"]

