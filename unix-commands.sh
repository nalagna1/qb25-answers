# 1. Explore ce11_genes.bed using Unix

unix-python-scripts % wc -l ce11_genes.bed
#    53935 ce11_genes.bed

cut -f1 ce11_genes.bed | sort | uniq -c
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

# 2. Recalculate ce11_genes.bed scores using Python

# For some reason, I'm having a hard time getting my scripts to run from the terminal.

#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as my_file:
    for line in my_file:
        fields = line.strip("\n").split("\t")
        chrom = fields[0]
        start = int(fields[1])
        end = int(fields[2])
        name = fields[3]
        score = int(fields[4])
        strand = fields[5]

        feature_size = end - start
        new_score = score * feature_size
        if strand == "-":
            new_score = -new_score

         print("\t".join([chrom, str(start), str(end), name, str(new_score), strand]))

# 3. Explore GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt using Unix

cut -f7 GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt | sort | uniq -c | sort -nr | head -3

grep -c "RNA" GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt

grep -vc "RNA" GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt

# 4. Transform GTEx data using Python

with open("GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_tpm.gct") as f:
    f.readline()  # skip first line
    f.readline()  # skip second line
    header = f.readline().strip().split("\t")
    data = f.readline().strip().split("\t")

expression_dict = {}
for i in range(2, len(header)):  # first 2 columns are gene info
    sample_id = header[i]
    expression_value = data[i]
    expression_dict[sample_id] = expression_value

with open("GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt") as f:
    for line in f:
        fields = line.strip().split("\t")
        sampid = fields[0]
        smtsd = fields[6]  # column 7 = SMTSD
        if sampid in expression_dict:
            print(sampid, expression_dict[sampid], smtsd, sep="\t")