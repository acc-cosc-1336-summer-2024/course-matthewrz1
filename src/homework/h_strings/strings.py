#function definition file HW 5

def get_hamming_distance(dna1, dna2):

    y = 0

    for x in range(0,len(dna1)):
        if dna1[x] != dna2[x]:
            y = y + 1
    
    return y

def get_dna_complement(dna):

    rev_dna = ''
    x = len(dna)-1

    while x >= 0:
        rev_dna = rev_dna + dna[x].upper()
        x = x - 1 
    
    complement = ''

    for i in range(0,len(rev_dna)):
        if rev_dna[i] == 'A':
            complement = complement + 'T'

        elif rev_dna[i] == 'T':
            complement = complement + 'A'

        elif rev_dna[i] == 'G':
            complement = complement + 'C'

        elif rev_dna[i] == 'C':
            complement = complement + 'G'
    
    return complement