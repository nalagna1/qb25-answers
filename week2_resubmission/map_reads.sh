#!/bin/bash

for sample in A01_01 A01_02 A01_03 A01_04 A01_05 A01_06
do
    echo "*** $sample"
    # Mapping: output SAM file
    bowtie2 -p 4 -x ../genomes/sacCer3 -U ../BYxRM/fastq/${sample}.fq.gz > ${sample}.sam

    # Sorting: input SAM output BAM
    samtools sort -o ${sample}.bam ${sample}.sam

    # Indexing BAM
    samtools index ${sample}.bam
done