# Write a program that calculates the factorial of a number.

n = int(input("Enter a number: "))

result = 1

for i in range(1, n+1):
  result = result * i
  i - 1

print(result)
