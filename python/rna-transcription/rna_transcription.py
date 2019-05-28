def to_rna(dna_strand):
    split_rna = [i for i in dna_strand]
    rna_trans = {'C':'G', 'G':'C','T':'A','A':'U'}
    rna_strand = ''.join(([rna_trans.get(l, l) for l in split_rna]))
    return rna_strand


    
to_rna('ACGTGGTCTTAA')  