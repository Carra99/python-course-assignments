sequence = input("Please enter a DNA sequence: ").upper()
valid_chars = {"A", "C", "G", "T"}

if all(c not in valid_chars for c in sequence):
    print("No valid DNA characters found.")
    exit()

fragments = []
current = [] 

for c in sequence: 
    if c in valid_chars:
        current.append(c)
    else:
        if current:
            fragments.append("".join(current))
            current = []

if current:
    fragments.append("".join(current))

sorted_fragments = sorted(fragments, key=len, reverse=True) 

print(sorted_fragments)    
 
