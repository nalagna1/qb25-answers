#!/bin/bash

set -e

cd BYxRM_bam

for bam in *.bam; do
    samtools index $bam
done

rm -f read_counts.txt
for bam in *.bam; do
    count=$(samtools view -c $bam)
    echo "$bam $count" >> read_counts.txt
done

ls *.bam > bamListFile.txt

ref_genome="../sacCer3.fasta"
ploidy=1

freebayes -f $ref_genome -L bamListFile.txt --genotype-qualities -p $ploidy > unfiltered.vcf

vcffilter -f "QUAL > 20" -f "AN > 9" unfiltered.vcf > filtered.vcf
vcfallelicprimitives -kg filtered.vcf > decomposed.vcf
vcfbreakmulti decomposed.vcf > biallelic.vcf

echo "Variant calling completed"