# Write a program that determines if a year is a leap year or not.

year = int(input("Enter the year: "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("It is a leap year.")
    else:
      print("It is not a leap year.")
  else:
    print("It is a leap year.")
else:
  print("It is not a leap year.")

