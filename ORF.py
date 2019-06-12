from Bio import SeqIO
from Bio import Alphabet

def getProts(prot):
    matches = []
    for i in range(len(prot)):
        if prot[i] == 'M':
            start = i
            for j in range(start, len(prot)):
                if prot[j] == '*':
                    matches.append(prot[start:j])
                    break
    return matches

def main():
    proteins = []
    matches = []
    codingStrand = SeqIO.read('orf.fna', 'fasta', alphabet = Alphabet.IUPAC.unambiguous_dna)
    for strand in [codingStrand.seq, codingStrand.seq.reverse_complement()]:
        for i in range(3):
            length = 3 * ((len(strand) - i) // 3)
            prots = strand[i:length+i].translate()
            proteins.append(str(prots))
    for j in proteins:
        matches += getProts(j)
    matches = set(matches)
    for k in matches:
        print(k)
                    
                

main()
