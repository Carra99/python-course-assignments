import random as rand

numb = rand.randint(1, 20)
debug_mode = False  # Flag to track debug mode

print("------------------------------------")
print("Welcome to the number guessing game!")
print("------------------------------------")
print("[FUNCTION KEYS] Press 'x' to exit, 's' to show the hidden number once, or 'd' to toggle debug mode.")

while True:
    if debug_mode:
        print(f"[DEBUG MODE] Hidden number: {numb}")

    user_input = input("Guess a whole number between 1 and 20 (or press 'x', 's', 'd'): ").lower()
    
    if user_input == "x":
        print("You exited the game. Goodbye!")
        break
    elif user_input == "s":
        print(f"You entered cheat mode. The hidden number is: {numb}")
        continue
    elif user_input == "d":
        debug_mode = not debug_mode
        status = "ON" if debug_mode else "OFF"
        print(f"Debug mode is now {status}.")
        continue

    guess = int(user_input)

    if numb > guess:
        print("Your guess is too low.")
    elif numb < guess:
        print("Your guess is too high.")
    else:
        print("Congratulations! You guessed the number!")
        break

    print("Try again!")
