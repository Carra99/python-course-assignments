import sys
from collections import Counter

if len(sys.argv) != 2:
    print("Usage: python count_digits_in_file.py <path_to_input_file>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, 'r', encoding='utf-8') as f:
    text = f.read()

# Count only digits
digits = [char for char in text if char.isdigit()]
counter = Counter(digits)

with open('report.txt', 'w') as report:
    for digit in map(str, range(10)):  # Ensures we include '0' to '9'
        count = counter.get(digit, 0)
        line = f"{digit} {count}"
        print(line)
        report.write(line + '\n')
