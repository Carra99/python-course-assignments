import sys 

if len(sys.argv) !=2:
    print("Usage: python dna_sequencing.py <dna_sequence>")
    print("Accepted characters: A, C, G, T and X only")
    sys.exit() 

sequence = sys.argv[1].upper()
valid_chars = {"A", "C", "G", "T", "X"}

#check for invalid characters
invalid = [c for c in sequence if c not in valid_chars]
if invalid:
    print(f"Invalid characters found: {', '.join(invalid)}")
    print("Accepted characters: A, C, G, T and X only")
    sys.exit()

#split the sequence by "X" 
fragments = [part for part in sequence.split("X") if part]
sorted_fragments = sorted(fragments, key=len, reverse=True) 

print(sorted_fragments) 

