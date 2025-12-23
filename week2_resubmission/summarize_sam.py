import sys

samfile = sys.argv[1]

chrom_counts = {}
nm_counts = {}

with open(samfile) as f:
    for line in f:
        if line.startswith('@'):
            continue
        parts = line.strip().split('\t')
        rname = parts[2]
        chrom_counts[rname] = chrom_counts.get(rname, 0) + 1
        # Find NM tag
        for field in parts[11:]:
            if field.startswith('NM:i:'):
                nmval = int(field[5:])
                nm_counts[nmval] = nm_counts.get(nmval,0) + 1

for k, v in chrom_counts.items():
    print(f'{k}\t{v}')

print("\nNM tag counts:")
for nm in sorted(nm_counts):
    print(f'{nm}\t{nm_counts[nm]}')