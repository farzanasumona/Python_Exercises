# Write a program that checks if a given number is prime or not.

number = int(input("Enter a number: "))

is_prime = True

for i in range(2, 11):
  if number % i == 0:
    is_prime = False
    break

if is_prime == False:
  print(f"{number} is not a prime number")
else:
  print(f"{number} is a prime number")
