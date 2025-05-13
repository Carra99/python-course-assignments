import random as rand

numb = rand.randint(1, 20)
print("------------------------------------")
print("Welcome to the number guessing game!")
print("Type 'x' to exit the game.")
print("------------------------------------")

while True:
    user_input = input("Guess a whole number between 1 and 20 (or press 'x' to exit): ")
    
    if user_input.lower() == "x":
        print("You exited the game. Goodbye!")
        break
    
    guess = int(user_input)    

    if numb > guess:
        print("Your guess is too low.")
    elif numb < guess:
        print("Your guess is too high.")
    else:
        print("Congratulations! You guessed the number!")
        break
    print ("Try again!")
