# Finding the share k-mers # Quiz

# Function # Shared k-mers
def reverse_complement(kmer):
    """Return the reverse complement of a DNA k-mer."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    # Reverse the k-mer and substitute each nucleotide by its complement.
    return "".join(complement[base] for base in reversed(kmer))

def shared_kmers(genome1, genome2, k):
    """
    Find all shared k-mers between genome1 and genome2.
    
    A k-mer from genome1 (starting at position x) is considered shared if 
    either it or its reverse complement appears in genome2 at some position y.
    
    Returns a list of (x, y) pairs.
    """
    pairs = []
    for x in range(len(genome1) - k + 1):
        kmer1 = genome1[x:x+k]
        rc_kmer1 = reverse_complement(kmer1)
        for y in range(len(genome2) - k + 1):
            kmer2 = genome2[y:y+k]
            if kmer1 == kmer2 or rc_kmer1 == kmer2:
                pairs.append((x, y))
    return pairs

# Example usage 1
# Input genomes and k value
genome1 = "AAACTCATC"
genome2 = "TTTCAAATC"
k = 2

# Compute shared k-mers
pairs = shared_kmers(genome1, genome2, k)

# Output
print("Shared {}-mer pairs:".format(k))
for pair in pairs:
    print(pair)
print("\nTotal shared {}-mers: {}".format(k, len(pairs)))

'''
Output
Shared 2-mer pairs:
(0, 0)
(0, 1)
(0, 4)
(0, 5)
(1, 0)
(1, 1)
(1, 4)
(1, 5)
(4, 2)
(4, 7)
(5, 3)
(6, 6)
(7, 2)
(7, 7)

Total shared 2-mers: 14
'''

# Example usage 2
# Exam  # Shared k-mers
# Input genomes and k value
genome1 = "TGCCCCGGTGGTGAG"
genome2 = "AAGGTCGCACCTCGT"
k = 3

# Compute shared k-mers
pairs = shared_kmers(genome1, genome2, k)

# Output the results
print("Shared {}-mer pairs:".format(k))
for pair in pairs:
    print(pair)
print("\nTotal shared {}-mers: {}".format(k, len(pairs)))

'''
Output
Shared 3-mer pairs:
(0, 6)
(6, 2)
(6, 8)
(7, 7)
(9, 2)
(9, 8)
(10, 7)
(12, 10)

Total shared 3-mers: 8
'''
