# Write a program that generates a Fibonacci sequence of length `n`.

n = int(input("Enter a positive number: "))

previous = 0
current = 1

print(previous)
print(current)

for i in range(3, n+1):
  f_sum = previous + current
  print(f_sum)
  previous = current
  current = f_sum
