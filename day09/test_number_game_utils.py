
from number_game_utils import generate_number, toggle_mode, process_guess, shift_number

def test_generate_number():
    for _ in range(100):
        num = generate_number()
        assert 1 <= num <= 20

def test_toggle_mode():
    assert toggle_mode(True) == False
    assert toggle_mode(False) == True

def test_process_guess():
    assert process_guess(5, 10) == 'low'
    assert process_guess(15, 10) == 'high'
    assert process_guess(10, 10) == 'correct'

def test_shift_number():
    for i in range(1, 21):
        shifted = shift_number(i)
        assert 1 <= shifted <= 20
