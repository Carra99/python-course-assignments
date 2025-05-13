import random as rand

numb = rand.randint(1, 20)
debug_mode = False 
move_mode = False

print("------------------------------------")
print("Welcome to the number guessing game!")
print("------------------------------------")
print("[FUNCTION KEYS] Press 'x' to exit, 's' to show the hidden number once, 'd' to toggle debug mode, 'm' to toggle move mode, or 'n' to start a new game.")

while True:
    if debug_mode:
        print(f"[DEBUG MODE] Hidden number: {numb}")

    user_input = input("Guess a whole number between 1 and 20 (or press 'x', 's', 'd', 'm', 'n'): ").lower()
    
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
    elif user_input == "m":
        move_mode = not move_mode
        status = "ON" if move_mode else "OFF"
        print(f"Move mode is now {status}.")
        continue
    elif user_input == "n":
        numb = rand.randint(1, 20)
        print("A new game started! A new number has been generated.")
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

    if move_mode:
        shift = rand.randint(-2, 2)
        old_numb = numb
        numb += shift
        numb = max(1, min(20, numb)) 

        if debug_mode:
            print(f"[DEBUG MODE] The number has shifted from {old_numb} to {numb}.")
