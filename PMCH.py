from Bio import SeqIO
from math import factorial

def main():
    strand = SeqIO.read('pmch.fna', 'fasta').seq
    print(factorial(int(strand.count('A'))) * factorial(int(strand.count('G'))))

main()
