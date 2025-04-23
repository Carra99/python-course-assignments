import random

rand_numb = random.randint(1, 20)
guess = int(input("Guess a number between 1 and 20: " ))

if guess < rand_numb:
    print("The number is too low!")
elif guess > rand_numb:
    print("The number is too high!")
else:
    print("Correct! You guessed the number")
