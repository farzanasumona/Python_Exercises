# Write a program that finds the greatest common divisor (GCD) of two numbers.

print("Greatest Common Divisor (GCD) Finder")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

a = num1
b = num2

while b != 0:
    a, b = b, a % b

print(f"The GCD of {num1} and {num2} is: {a}")

