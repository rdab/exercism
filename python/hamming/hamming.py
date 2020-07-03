def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strand length differ')
    return sum(map(lambda x,y: 1 if x!=y else 0, iter(strand_a), iter(strand_b)))
