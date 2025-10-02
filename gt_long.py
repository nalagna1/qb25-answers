
vcf_file = "biallelic.vcf"
sample_ids = ["A01_62", "A01_39", "A01_63", "A01_35", "A01_31", "A01_27", "A01_24", "A01_23", "A01_11", "A01_09"]

with open(vcf_file) as f_vcf, open("gt_long.txt", "w") as out:
    out.write("sample\tchrom\tpos\tgt\n")
    for line in f_vcf:
        if line.startswith("#"):
            continue
        fields = line.rstrip('\n').split('\t')
        chrom = fields[0]
        pos = fields[1]
        format_keys = fields[8].split(":")
        gt_i = format_keys.index("GT")
        for i, sname in enumerate(sample_ids):
            sample_str = fields[9+i]
            gt_val = sample_str.split(":")[gt_i]
            if gt_val in ["0", "1"]:
                out.write(f"{sname}\t{chrom}\t{pos}\t{gt_val}\n")