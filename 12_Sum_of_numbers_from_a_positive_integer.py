#sum of numbers from a positive integer
Positive_integer = int(input("Positive Number: "))

total = 0
sum = Positive_integer

while sum > 0:
    total += sum
    sum -= 1
print("User entered integer: ",Positive_integer)
print("Sum found by the while loop: ", total)