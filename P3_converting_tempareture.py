# Write a program that converts temperature from Fahrenheit to Celsius.

fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print("Temperature in Celsius:", round(celsius, 2))

