def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strand length differ')
    return sum(map(lambda x,y: x!=y, iter(strand_a), iter(strand_b)))
