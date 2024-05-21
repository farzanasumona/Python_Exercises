# Write a program that finds the sum of all even numbers between 1 and `n`.

n = int(input("Enter a number: "))

sum_of_even = 0

i = 1

while i <= n:
  if i % 2 == 0:
    sum_of_even += i
  i += 1

print(sum_of_even)
