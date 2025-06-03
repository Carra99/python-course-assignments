import sys
from collections import Counter

# Codon to amino acid dictionary
codon_table = {
    'Phe': ['TTT', 'TTC'],
    'Leu': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile': ['ATT', 'ATC', 'ATA'],
    'Met': ['ATG'],
    'Val': ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro': ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr': ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala': ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr': ['TAT', 'TAC'],
    'His': ['CAT', 'CAC'],
    'Gln': ['CAA', 'CAG'],
    'Asn': ['AAT', 'AAC'],
    'Lys': ['AAA', 'AAG'],
    'Asp': ['GAT', 'GAC'],
    'Glu': ['GAA', 'GAG'],
    'Cys': ['TGT', 'TGC'],
    'Trp': ['TGG'],
    'Arg': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly': ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP': ['TAA', 'TAG', 'TGA']
}

codon_to_aa = {}
for aa, codons in codon_table.items():
    for codon in codons:
        codon_to_aa[codon] = aa

if len(sys.argv) != 2:
    print("Usage: python count_amino_acids.py <dna_sequence_file.txt>")
    sys.exit(1)

filename = sys.argv[1]

# Read sequence
with open(filename, 'r') as f:
    sequence = f.read().upper().replace('\n', '').replace(' ', '')

# Split into codons (triplets)
codons = [sequence[i:i+3] for i in range(0, len(sequence), 3) if len(sequence[i:i+3]) == 3]

# Translate to amino acids
amino_acids = [codon_to_aa.get(codon, '???') for codon in codons]

# Count and print amino acid occurrences
counter = Counter(amino_acids)

for aa in sorted(counter):
    print(f"{aa:<10} {counter[aa]}")

