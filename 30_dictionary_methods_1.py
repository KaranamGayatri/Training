#create a variable and assign
songs = {"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive", "U2": "One", "Michael Jackson": "Billie Jean", "The Beatles": "Hey Jude", "Bob Dylan": "Like A Rolling Stone"}

#make the dictionary span multiple lines so that the line the dictionary starts on is not too long
songs = {"Queen": "Bohemian Rhapsody", 
         "Bee Gees": "Stayin' Alive", 
         "U2": "One", 
         "Michael Jackson": "Billie Jean", 
         "The Beatles": "Hey Jude", 
         "Bob Dylan": "Like A Rolling Stone"}

#print the length of the dictionary
print(len(songs))

#use the .keys() method and a for loop to get and print all of the keys from the dictionary on separate lines
for key in songs.keys():
    print(key)