#Celsius to fahrenheit with round
Celsius = int(input("Enter celsius temperature:"))
F = 1.8*Celsius+32
def fahrenheit(Celsius):
     return round(F,1)
print("The Fahrenheit equivalent of " +str(Celsius)+ " degrees Celsius is " +str(fahrenheit(Celsius)))