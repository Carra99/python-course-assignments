import random as rand

numb = rand.randint(1, 20)
print("------------------------------------")
print("Welcome to the number guessing game!")
print("------------------------------------")

max_attempts = 5
attempts = 0

while attempts < max_attempts:
    guess = int(input("You have 5 attempts. Guess a whole number between 1 and 20: "))
    attempts += 1 

    if numb > guess:
        print("Your guess is too low.")
    elif numb < guess:
        print("Your guess is too high.")
    else:
        print("Congratulations! You guessed the number!")
        break
    
    if attempts < max_attempts:
        print(f"You have {max_attempts - attempts} attempts left. Try again!")
    
if attempts == max_attempts and guess != numb:
    print("You have used all your attempts.")

print ("Thanks for playing!")
