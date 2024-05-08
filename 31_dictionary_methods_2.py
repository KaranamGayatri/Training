#use .fromkeys() to create a dictionary
for key, value in {}.fromkeys("bcdefghijklmnopqrstuvwxyz","consonant").items():
    print(key, value)

#pop and print "Big Mac"
fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
print(fast_food_items.pop("McDonald's"))
 