from Bio import SeqIO

def main():
    inputs = [str(i.seq) for i in SeqIO.parse('sseq.fna', 'fasta')]
    mainStr = inputs[0]
    subStr = inputs[1]
    results = []
    start = 0
    for j in subStr:
        hit = mainStr[start:].find(j)
        results.append(str(hit+start+1))
        start = hit+start+1
    print(' '.join(results))

main()
