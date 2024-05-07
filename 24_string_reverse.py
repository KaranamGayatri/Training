#Creating a variable and assigning it a string as user input
String = input("Enter a String: ")
#Create a variable before the for loop and assign it an empty string
Reversed_string = ""
#Using for loop
for i in range(len(String)-1,-1,-1):
    Reversed_string += String[i]
#print the reversed string
print("Reversed string: ", Reversed_string)
