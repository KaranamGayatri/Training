#Create two dictionaries
internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}

#use .update() to add the contents of another_one to internet_celebrities
internet_celebrities.update(another_one)

#create a variable and assign it a copy of internet_celebrities
celebrities = internet_celebrities.cop()