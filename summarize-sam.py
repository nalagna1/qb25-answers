import sys
from collections import defaultdict

filename = sys.argv[1]
chr_counts = defaultdict(int)
nm_counts = defaultdict(int)

with open(filename) as f:
    for line in f:
        if line.startswith('@'): continue
        fields = line.strip().split('\t')
        chr = fields[2]
        chr_counts[chr] += 1
        # Find NM tag
        for field in fields[11:]:
            if field.startswith('NM:i:'):
                nm = int(field[5:])
                nm_counts[nm] += 1

for k in chr_counts.keys():
    print(f"{k}\t{chr_counts[k]}")
print("--- NM counts ---")
for k in sorted(nm_counts.keys()):
    print(f"{k}\t{nm_counts[k]}")

# Run with python3 summarize-sam.py A01_01.sam > summarize-sam.txt
          