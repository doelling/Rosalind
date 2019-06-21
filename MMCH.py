from Bio import SeqIO
from math import factorial

def main():
    strand = SeqIO.read('mmch.fna', 'fasta').seq
    au = sorted([int(strand.count('A')), int(strand.count('U'))])
    gc = sorted([int(strand.count('G')), int(strand.count('C'))])
    auComb = factorial(au[1])//factorial(au[1]-au[0])
    gcComb = factorial(gc[1])//factorial(gc[1]-gc[0])
    print(auComb * gcComb)

main()
