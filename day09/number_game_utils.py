
import random

def generate_number():
    """
    Generates a random number between 1 and 20.

    Returns:
        int: a random number from 1 to 20

    Example:
        >>> num = generate_number()
        >>> 1 <= num <= 20
        True
    """
    return random.randint(1, 20)

def toggle_mode(current_mode):
    """
    Toggles a boolean mode (e.g., debug, move).

    Args:
        current_mode (bool): current state of the mode

    Returns:
        bool: toggled state

    Example:
        >>> toggle_mode(False)
        True
    """
    return not current_mode

def process_guess(guess, target):
    """
    Compares a guess to the target number.

    Args:
        guess (int): the player's guess
        target (int): the correct number

    Returns:
        str: 'low', 'high', or 'correct'

    Example:
        >>> process_guess(5, 10)
        'low'
    """
    if guess < target:
        return 'low'
    elif guess > target:
        return 'high'
    return 'correct'

def shift_number(numb):
    """
    Shifts the number randomly between -2 and 2, stays in range [1, 20].

    Args:
        numb (int): current number

    Returns:
        int: shifted number

    Example:
        >>> shifted = shift_number(10)
        >>> 1 <= shifted <= 20
        True
    """
    shift = random.randint(-2, 2)
    return max(1, min(20, numb + shift))
