#!/bin/bash

for sample in A01_01 A01_02 A01_03 A01_04 A01_05 A01_06
do
    echo "***" $sample
    bowtie2 -p 4 -x ../genomes/sacCer3 -U fastq/${sample}.fq.gz -S ${sample}.sam
    samtools sort -o ${sample}.bam ${sample}.sam
    samtools index ${sample}.bam
done

# The visualization in IGV for chrI:27,000-32,000 reflects genotypes in BYxRM_GenoData.txt. Each .bam file shows read coverage and variants at marker positions. We can see, for example, that sample A01_01 matches allele R at chrI:27915, consistent with the genotype table.