from collections import Counter

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def count_words(text):
    words = text.lower().split()
    return Counter(words)

def display_word_counts(counter):
    for word in sorted(counter):
        print(f"{word:<15} {counter[word]}")
