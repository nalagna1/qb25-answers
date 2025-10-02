
import pandas as pd

df = pd.read_csv("gt_long.txt", sep="\t")
crosscount = {}

for sample in df['sample'].unique():
    cros = 0
    prev = None
    for chrom in df['chrom'].unique():
        sub = df[(df['sample'] == sample) & (df['chrom'] == chrom)].sort_values('pos')
        lastgt = None
        for i, row in sub.iterrows():
            currgt = row['gt']
            if lastgt is not None and currgt != lastgt:
                cros += 1
            lastgt = currgt
    crosscount[sample] = cros

with open("crossovers.txt", "w") as f:
    for s, c in crosscount.items():
        f.write(f"{s}\t{c}\n")