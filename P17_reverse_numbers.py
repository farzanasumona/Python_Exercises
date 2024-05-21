# Write a program that reverses a given number.

number = int(input("Enter a number: "))

number_list = list(str(number))

reversed_list = []

index = len(number_list) - 1

while index >= 0:
  reversed_list.append(number_list[index])
  index -= 1

result = int(''.join(reversed_list))

print(result)
