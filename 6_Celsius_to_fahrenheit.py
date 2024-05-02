#Celsius to Fahrenheit
Celsius = int(input("Enter celsius temperature:"))
F = 1.8*Celsius+32
def fahrenheit(Celsius):
     return(F)
print("The Fahrenheit equivalent of " +str(Celsius)+ "degrees Celsius is " +str(fahrenheit(Celsius)))