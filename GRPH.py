from Bio import SeqIO
import itertools

def overlapThree(strA, strB):
    return strA[-3:] == strB[:3]
        

def main():
    dnaStrands = {str(i.id): str(i.seq) for i in SeqIO.parse('grph.fna', 'fasta')}
    for j, k in itertools.combinations(dnaStrands.keys(), 2):
        jStrand, kStrand = dnaStrands[j], dnaStrands[k]
        if jStrand[-3:] == kStrand[:3]:
            print(j + ' ' + k)
        if kStrand[-3:] == jStrand[:3]:
            print(k + ' ' + j)

main()
