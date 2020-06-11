import re
from Bio.Seq import Seq
from Bio.Seq import IUPAC
from Bio.Blast import NCBIWWW, NCBIXML


def check_seq(seq):
    desc = ''
    transc = ''
    transl = ''
    soort = 0
    if re.search("^[ACTG]*$", seq):
        seq = Seq(seq, IUPAC.unambiguous_dna)
        transc = convert_rna(seq)
        transl = convert_protein(transc)
        print(transc)
        print(transl)
        desc = find_gene(seq)
        soort = 1
    elif re.search("^[ACUG]*$", seq):
        seq = Seq(seq, IUPAC.unambiguous_rna)
        transl = convert_protein(seq)
        soort = 2
    else:
        seq = Seq(seq, IUPAC.protein)
        soort = 3
    return desc, transc, transl, soort


def convert_rna(seq):
    trans = seq.transcribe()
    return trans


def convert_protein(transc):
    transl = transc.translate()
    return transl


def find_gene(seq):
    result = NCBIWWW.qblast('blastx', 'nr', seq, hitlist_size=10)
    blast_records = NCBIXML.read(result)
    desc = blast_records.alignments[0].title
    return desc


if __name__ == '__main__':
    check_seq(
        'TGTTAACGGTGTTCATGGTTAACCATCCATGATTGAACCACTCGAATCTGAAGGAGTGACGGCATGCGCCGTATCGCAGCCATTACAAGAAATCCGGTAGCCATCGCTATTGTCGCTGCCCTGGCGGTTGCTGGTTGTCGATCCAAGTCCGTTCCGAATAGTGCCGCAGACCTTGGCATCGGTGCCGGTGGCTCTGGAGCCGGAGGATCGCTCGGTTCAGCCGCCGCCGGCTCCCCGCAGGAGTTCCCCGCCACCGGCGGTCACCGGCTCATCTTTCCACACGGTTCACCGGTGCACCGTG')
