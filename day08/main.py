
import sys
from word_counter import read_file, count_words, display_word_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    filename = sys.argv[1]
    text = read_file(filename)
    counter = count_words(text)
    display_word_counts(counter)

if __name__ == "__main__":
    main()
