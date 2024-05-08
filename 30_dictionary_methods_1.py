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

#print all of the values from the dictionary using the .values() method
print(songs.values())

#use .items() with a for loop to iterate through and print all of the key value pairs from the dictionary
for key, value in songs.items():
    print(key, value)

#use the .get() method to check the dictionary for the key and create a message that will print if the key is not found in the dictionary
print(songs.get("Promise of the Real", "The key is not found in the dictionary." ))
