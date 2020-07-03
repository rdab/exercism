
mapping = str.maketrans('GCTA', 'CGAU')

def to_rna(dna_strand):
    return dna_strand.translate(mapping)
