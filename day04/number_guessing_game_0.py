import random as rand

numb = rand.randint(1, 20)
print("------------------------------------")
print("Welcome to the number guessing game!")
print("------------------------------------")
guess = int(input("Guess a whole number between 1 and 20: "))

if numb > guess:
    print("Your guess is too low.")
elif numb < guess:
    print("Your guess is too high.")
else:
    print("Congratulations! You guessed the number!")
print("Thanks for playing!")
