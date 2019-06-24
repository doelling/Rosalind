from Bio import SeqIO
import sys

sys.setrecursionlimit(5000)

lookup = []

def findLongest(seq1, seq2, x, y):
    if x == 0 or y == 0:
        return ''
    if seq1[x-1] == seq2[y-1]:
        return findLongest(seq1, seq2, x-1, y-1) + seq1[x-1]
    if lookup[x-1][y] > lookup[x][y-1]:
        return findLongest(seq1, seq2, x-1, y)
    else:
        return findLongest(seq1, seq2, x, y-1)

def fillTable(seq1, seq2, L1, L2):
    for i in range(1, L1):
        for j in range(1, L2):
            if seq1[i-1] == seq2[j-1]:
                lookup[i][j] = lookup[i-1][j-1] + 1
            else:
                lookup[i][j] = max(lookup[i-1][j], lookup[i][j-1])
            

def main():
    seqs = [str(i.seq) for i in SeqIO.parse('lcsq.fna', 'fasta')]
    seq1, seq2 = seqs[0], seqs[1]
    L1, L2 = len(seq1), len(seq2)
    for i in range(L1):
        lookup.append([0 for j in range(L2)])
    fillTable(seq1, seq2, L1, L2)
    print(findLongest(seq1, seq2, L1-1, L2-1))

main()
