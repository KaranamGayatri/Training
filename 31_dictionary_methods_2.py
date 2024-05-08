#use .fromkeys() to create a dictionary
for key, value in {}.fromkeys("bcdefghijklmnopqrstuvwxyz","consonant").items():
    print(key, value)