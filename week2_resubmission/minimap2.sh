#!/bin/bash

# Step 1: Align reads to genome, output SAM
minimap2 -ax map-ont sacCer3.fa ERR8562476.fastq > longreads.sam

# Step 2: Sort SAM to BAM
samtools sort -o longreads.bam longreads.sam

# Step 3: Index BAM
samtools index longreads.bam

# Step 4: Get idxstats
samtools idxstats longreads.bam > longreads.idxstats