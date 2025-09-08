
#!/usr/bin/env python3

import sys
import fasta

# Open fasta file
my_file = open(sys.argv[1])
contigs = fasta.FASTAReader(my_file)

contig_lengths = []
total_length = 0
count = 0

# Collect lengths
for ident, sequence in contigs:
    length = len(sequence)
    contig_lengths.append(length)
    total_length += length
    count += 1

# Calculate average length
average_length = total_length / count if count > 0 else 0

# Calculate N50
contig_lengths.sort(reverse=True)  # sort longest to shortest
cumulative = 0
n50 = 0

for length in contig_lengths:
    cumulative += length
    if cumulative >= total_length / 2:
        n50 = length
        break

# Print results
print(f"Number of contigs: {count}")
print(f"Total length: {total_length}")
print(f"Average length: {average_length:.2f}")
print(f"N50: {n50}")

# I can't figure out how to run this script from the terminal; it keeps telling me the file or directory doesn't exist.
# Make the script executable with chmod +x assembly-metrics.py
# Run the script with a specific file using (for example) ./assembly-metrics.py caenorhabditis_remanei.PRJNA248909.WBPS19.genomic.fa