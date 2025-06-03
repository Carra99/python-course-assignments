import sys
from collections import Counter

if len(sys.argv) != 2:
    print("Usage: python count_words_from_a_file.py <input_file>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, 'r', encoding='utf-8') as f:
    text = f.read()

# Split text into words
words = text.lower().split()
counter = Counter(words)

# Print results sorted alphabetically
for word in sorted(counter):
    print(f"{word:<15} {counter[word]}")
