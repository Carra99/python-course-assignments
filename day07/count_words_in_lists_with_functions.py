def get_celestial_objects():
    return ['Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid']

def count_words(words):
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

def print_word_count(counts):
    print(counts)

def main():
    objects = get_celestial_objects()
    word_counts = count_words(objects)
    print_word_count(word_counts)

if __name__ == "__main__":
    main()
