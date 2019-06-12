from Bio import SeqIO, motifs

def genCount(base, seqList, seqLen):
    counts = []
    for i in range(seqLen):
        tCount = 0
        for j in seqList:
            if j[i] == base:
                tCount += 1
        counts.append(str(tCount))
    return base + ': ' + ' '.join(counts)
    

def main():
    bases = ['A', 'C', 'G', 'T']
    seqs = []
    for i in SeqIO.parse('cons.fna', 'fasta'):
        seqs.append(i.seq)
    m = motifs.create(seqs)
    print(m.consensus)
    for j in bases:
        print(genCount(j, seqs, len(m)))
            

main()
