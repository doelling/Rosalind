from Bio import SeqIO, Alphabet

def main():
    strand = SeqIO.read('revp.fna', 'fasta', Alphabet.IUPAC.unambiguous_dna).seq
    for i in range(len(strand)):
        cond = len(strand) - i
        end = cond+1 if cond < 12 else 13
        for j in range(i+3, i+end):
            if strand[i:j] == strand[i:j].reverse_complement():
                print(str(i+1) + ' ' + str(len(strand[i:j])))
        

main()
