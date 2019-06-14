from Bio import SeqIO
from difflib import SequenceMatcher

def main():
    strings = [str(i.seq) for i in SeqIO.parse('lcsm.fna', 'fasta')]
    strings.sort(key=len)
    key = strings.pop(0)
    for j in range(len(strings)):
        if strings[j].find(key) != -1:
            continue
        else:
            seqMatch = SequenceMatcher(None, key, strings[j], False)
            match = seqMatch.find_longest_match(0, len(key), 0, len(strings[j]))
            key = key[match.a: match.a + match.size]
    print(key)
    
main()
