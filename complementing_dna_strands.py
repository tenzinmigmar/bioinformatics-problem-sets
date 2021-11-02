"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

with open ('testing_txt_files/rosalind_revc.txt') as f:
    x = f.read().rstrip("\n")

def complement_dna_strands(dnastr):
    mapping = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([mapping[i] for i in dnastr])[::-1]

print(complement_dna_strands(x))
