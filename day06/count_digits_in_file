import sys
from collections import Counter

if len(sys.argv) != 2:
    print("Usage: python count_digits_in_file.py <path_to_input_file>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, 'r', encoding='utf-8') as f:
    text = f.read()

digits = [char for char in text if char.isdigit()]
counter = Counter(digits)

with open('report.txt', 'w') as report:
    for digit in sorted(counter):
        line = f"{digit} {counter[digit]}"
        print(line)
        report.write(line + '\n')
