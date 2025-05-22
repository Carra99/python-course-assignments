celestial_objects = ['Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid']

word_count = {}
for word in celestial_objects:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
