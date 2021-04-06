#You can put Tuple in lists.
albums = [("Welcome to my nightmare", "Alice Cooper", 1975),
          ("Bad Comapany", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the lighting", "Metallica", 1984),
          ]

for album in albums: 
    #You can unpack the tuple. 
    title, artist, year = album
    print(f"The title of the album is {title}, The artists is {artist}, The year is {year}")

#Unpacking from the start. 
for album, artist, year in albums: 
    print(f"The title of the album is {album}, The artists is {artist}, The year is {year}")
