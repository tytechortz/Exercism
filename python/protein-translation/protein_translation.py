def proteins(strand):
    n = 3

    codons = [(strand[i:i+3]) for i in range(0, len(strand), n)]
    
    codon_protein = {
        'AUG':'Methionine',
        'UUU':'Phenylalanine',
        'UUC':'Phenylalanine',
        'UUA':'Leucine',
        'UUG':'Leucine',
        'UCU':'Serine',
        'UCC':'Serine',
        'UCA':'Serine',
        'UCG':'Serine',
        'UAU':'Tyrosine',
        'UAC':'Tyrosine',
        'UGU':'Cysteine',
        'UGC':'Cysteine',
        'UGG':'Tryptophan',
        }

    protein = []
    for codon in codons:
        if codon in ['UAA','UAG','UGA']:
            break
        else:
            protein.append(codon_protein.get(codon))
    return protein






