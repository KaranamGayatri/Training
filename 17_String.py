#Create a variable and assign it the string "Just do it!"
String = "Just do it!"

#Access the "!" from the variable by index and print() it
print(String[-1])

#Print the slice "do" from the variable
print(String[5:7])

#Get and print the slice "it!" from the variable
print(String[-3:])

#Print the slice "Just" from the variable
print(String[:4])

#Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".  Print the resulting string, which should be "Don't do it!" where the "do it!" part is a slice.
string_concatenate = "Don't" + String[4:]
print(string_concatenate)