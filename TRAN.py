from Bio import SeqIO

def main():
    strings = [str(j.seq) for j in SeqIO.parse('tran.fna', 'fasta')]
    subs = []
    for i in range(len(strings[0])):
        if strings[0][i] != strings[1][i]:
            subs.append((strings[0][i], strings[1][i]))
    trns = 0
    trv = 0
    for k in subs:
        if k[0] == 'A' or k[0] == 'G':
            if k[1] == 'A' or k[1] == 'G':
                trns += 1
            else:
                trv += 1
        else:
            if k[1] == 'C' or k[1] == 'T':
                trns += 1
            else:
                trv += 1
    print(trns/trv)

main()
