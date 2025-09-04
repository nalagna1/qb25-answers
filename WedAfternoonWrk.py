# Exercise 1
cut -f 5 ce11_genes.bed | sort | uniq -c
# 5460 chrI
# 6299 chrII
# 4849 chrIII
# 21418 chrIV
# 12 chrM
# 9057 chrV
# 6840 chrX
cut -f6 ce11_genes.bed | sort | uniq -c
# 26626 -
# 27309 +

# Exercise 2
#!/usr/bin/env python3

import sys

my_file = open(sys.argv[1])
my_file = my_file.strip("\n")
my_file = my_file.split("\t")

for bed_data in my_file:
    bed_data = my_file.split("\t")
    start = int(bed_data[1])
    end = int(bed_data[2])
    gene_length = end - start
    original_score = int(bed_data[4])
    new_score = original_score*gene_length
    if bed_data[5] == "-":
        new_score == new_score * -1
    else:
        continue
    if bed_data[5] == "+":
        new_score == new_score * 1