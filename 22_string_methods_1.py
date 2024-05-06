#Create a variable called mixed_case
mixed_case = "A Song of Ice and Fire"

#Use .isupper() to check if mixed_case is a string of all upper case letters
print(mixed_case.isupper())

#Use .islower() to check if mixed_case is a string of all lower case letters
print(mixed_case.islower())

#Change all of the letters in mixed_case to upper case letters using .upper()
print(mixed_case.upper())

#Change all of the letters in mixed_case to lower case letters using .lower()
print(mixed_case.lower())

#Use the .istitle() method to check if mixed_case is title case
print(mixed_case.istitle())

#Create a variable called title_case and assign it the result of .title() being called on mixed_case.
title_case = mixed_case.title()

#print() title_case
print(title_case)

#Call startswith() on mixed_case with the letter mixed_case starts with as its argument.
print(mixed_case.startswith('A'))

#Call endswith() on mixed_case with the letter mixed_case ends with as its argument
print(mixed_case.endswith('e'))

#Create a variable called words and assign it the result of split() being used on mixed_case
words = mixed_case.split()

#print the variable "words"
print(words)

