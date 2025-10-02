
vcf_file = "biallelic.vcf"

with open(vcf_file) as f_vcf, \
     open("AF.txt", "w") as f_af, \
     open("DP.txt", "w") as f_dp:

    f_af.write("AF\n")
    f_dp.write("DP\n")

    for line in f_vcf:
        if line.startswith("#"):
            continue
        fields = line.rstrip('\n').split('\t')

        info = fields[7]
        af_val = None
        for entry in info.split(";"):
            if entry.startswith("AF="):
                af_val = entry.split("=")[1]
                break

        if af_val is not None:
            f_af.write(f"{af_val}\n")

        format_keys = fields[8].split(":")
        if "DP" in format_keys:
            dp_i = format_keys.index("DP")
            for sample in fields[9:]:
                sample_fields = sample.split(":")
                if len(sample_fields) > dp_i:
                    dp_val = sample_fields[dp_i]
                    f_dp.write(f"{dp_val}\n")