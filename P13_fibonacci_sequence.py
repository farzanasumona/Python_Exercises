# Write a program that generates a Fibonacci sequence of length `n`.
n = int(input("Enter a number: "))

Previous = 0
current = 1

if n <= 0:
    result = []
elif n == 1:
    result = [Previous]
else:
    result = [Previous, current]

for i in range(2, n):
  f_sum = Previous + current
  result.append(f_sum)
  Previous = current
  current = f_sum
print(result)

