# Write a program that generates a random number and allows the user to guess it.

import random

number_to_guess = random.randint(1, 100)
guess = None

while guess != number_to_guess:
  guess = int(input("Enter your guess: "))
  if guess < number_to_guess:
    print("Too low! Try again.")
  elif guess > number_to_guess:
    print("Too high! Try again.")
  else:
    print("Congratulations! You guessed the number.")
    
