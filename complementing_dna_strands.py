"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

def complement_dna_strands(dnastr):
    mapping = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    for i in dnastr:


print(complement_dna_strands("ATGAGGTGATGTACCAGC"))