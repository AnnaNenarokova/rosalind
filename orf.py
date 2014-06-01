def translateDNA (DNA):    
    gene_code = dict(TTT = 'F', CTT = 'L', ATT = 'I', GTT = 'V', TTC ='F', CTC = 'L', ATC ='I',
    GTC = 'V', TTA = 'L', CTA = 'L', ATA = 'I', GTA = 'V', TTG = 'L', CTG = 'L', ATG = 'M', GTG = 'V',
    TCT = 'S', CCT = 'P', ACT = 'T', GCT = 'A', TCC = 'S', CCC = 'P', ACC = 'T', GCC = 'A', TCA = 'S',
    CCA = 'P', ACA = 'T', GCA = 'A', TCG = 'S', CCG = 'P', ACG = 'T', GCG = 'A', TAT = 'Y', CAT = 'H',
    AAT = 'N', GAT = 'D', TAC = 'Y', CAC = 'H', AAC = 'N', GAC = 'D', TAA = 'Stop', CAA = 'Q', AAA = 'K',
    GAA = 'E', TAG = 'Stop', CAG = 'Q', AAG = 'K', GAG = 'E', TGT = 'C', CGT = 'R', AGT = 'S', GGT = 'G',
    TGC = 'C', CGC = 'R', AGC = 'S', GGC  = 'G', TGA = 'Stop', CGA = 'R', AGA = 'R', GGA = 'G', TGG = 'W',
    CGG = 'R', AGG = 'R', GGG = 'G')
    peptide = ''
    for first in range (0, len(DNA), 3):
        last = first + 3
        codon = DNA[first : last]
        if codon in gene_code:
            if gene_code[codon] == 'Stop': break
            else:
                peptide = peptide + gene_code[codon]
        else:
            print 'error'
    return peptide


seq = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'

start_codons = [m.start() + 1 for m in re.finditer('(?=ATG)', seq)]
print start_codons
stop_codons = [m.start() + 1 for m in re.finditer('(?=TAG)', seq)]
print stop_codons