#factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
numbers = [3, 4, 5]
for num in numbers:
    print("Factorial of ", num, "is " ,factorial(num))