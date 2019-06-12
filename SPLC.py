from Bio import SeqIO
from Bio import Alphabet
from Bio.Seq import Seq
import re

def main():
    introns = [str(i.seq) for i in SeqIO.parse('splc.fna', 'fasta', Alphabet.IUPAC.unambiguous_dna)]
    mainSeq = introns.pop(0)
    exon = re.sub('|'.join(introns), '', mainSeq)
    print(Seq(exon, Alphabet.IUPAC.unambiguous_dna).translate(to_stop=True))
    
main()
