# Write a program that prints the multiplication table of a given number.

n = int(input("Enter a number: "))

for i in range(1, 11):
  multi_table = n * i
  print(f"{n} x {i} = ", multi_table)
