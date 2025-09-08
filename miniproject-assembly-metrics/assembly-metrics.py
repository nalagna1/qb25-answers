#!/usr/bin/env python3

import sys
import fasta

my_file = open(sys.argv[1])
contigs = fasta.FASTAReader(my_file)

contig_lengths = []
total_length = 0
count = 0

for ident, sequence in contigs:
    length = len(sequence)
    contig_lengths.append(length)
    total_length += length
    count += 1

average_length = total_length / count if count > 0 else 0

print(f"Number of contigs: {count}")
print(f"Total length: {total_length}")
print(f"Average length: {average_length:.2f}")

contig_lengths.sort(reverse=True)  # longest → shortest
half_total = total_length / 2
cumulative = 0
N50 = None

for length in contig_lengths:
    cumulative += length
    if cumulative >= half_total:
        N50 = length
        break

print(f"N50: {N50}")

# I can't figure out how to run this script from the terminal; it keeps telling me the file or directory doesn't exist.
# Make the script executable with chmod +x assembly-metrics.py
# Run the script with a specific file using ./assembly-metrics.py caenorhabditis_remanei.PRJNA248909.WBPS19.genomic.fa