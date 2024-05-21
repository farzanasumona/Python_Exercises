# Write a program that checks if a given string, is a palindrome.

number = input("Enter a number: ")

number_list = list(number)

reversed_list = []

index = len(number_list) - 1

while index >= 0:
  reversed_list.append(number_list[index])
  index -= 1

result = str(''.join(reversed_list))

if number == result:
  print("It is a palindrome")
else:
  print("It is not a palindrome")

