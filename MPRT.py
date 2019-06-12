from Bio import ExPASy, SwissProt

def findNGlycMotif(sequence):
    hits = []
    for i in range(len(sequence)-4):
        if sequence[i] == 'N':
            if sequence[i+1] != 'P':
                if sequence[i+2] == 'S' or sequence[i+2] == 'T':
                    if sequence[i+3] != 'P':
                        hits.append(str(i+1))
    return ' '.join(hits)

def main():
    proteins = []
    seqs = []
    f = open('mprt.txt', 'r')
    for line in f.readlines():
        proteins.append(str(line).strip('\n'))
    for i in proteins:
        handle = ExPASy.get_sprot_raw(i)
        record = SwissProt.read(handle)
        seqs.append(str(record.sequence))
    protDict = dict(zip(seqs, proteins))
    for j in protDict.keys():
        hitIndex = findNGlycMotif(j)
        if hitIndex != '':
            print(protDict[j])
            print(hitIndex)

main()
