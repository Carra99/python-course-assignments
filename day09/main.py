
from number_game_utils import generate_number, toggle_mode, process_guess, shift_number

def run_game():
    numb = generate_number()
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
            debug_mode = toggle_mode(debug_mode)
            print(f"Debug mode is now {'ON' if debug_mode else 'OFF'}.")
            continue
        elif user_input == "m":
            move_mode = toggle_mode(move_mode)
            print(f"Move mode is now {'ON' if move_mode else 'OFF'}.")
            continue
        elif user_input == "n":
            numb = generate_number()
            print("A new game started! A new number has been generated.")
            continue

        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number or a command key.")
            continue

        result = process_guess(guess, numb)
        if result == 'low':
            print("Your guess is too low.")
        elif result == 'high':
            print("Your guess is too high.")
        else:
            print("Congratulations! You guessed the number!")
            break

        print("Try again!")

        if move_mode:
            old_numb = numb
            numb = shift_number(numb)
            if debug_mode:
                print(f"[DEBUG MODE] The number has shifted from {old_numb} to {numb}.")

if __name__ == "__main__":
    run_game()
