def distance(strand_a, strand_b):
    
    if len(strand_a) == len(strand_b):
        hamming = len(strand_a)
        for x in range(len(strand_a)):
            if strand_a[x] == strand_b[x]:
                hamming -= 1
        print(hamming)
        return hamming

    else:
        raise ValueError("Lengths not matching")
    


# distance("GO", "T")