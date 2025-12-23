Part 1

cd ~/Data/genomes
cp ~/Data/References/sacCer3/sacCer3.fa.gz .
gunzip sacCer3.fa.gz
bowtie2-build sacCer3.fa sacCer3

cd ~/Data/variants
bowtie2 -p 4 -x ../genomes/sacCer3 -U ../BYxRM/fastq/A01_01.fq.gz > A01_01.sam
samtools sort -o A01_01.bam A01_01.sam
samtools index A01_01.bam
samtools idxstats A01_01.bam > A01_01.idxstats

Output:
740067 reads; of these:
  740067 (100.00%) were unpaired; of these:
    3135 (0.42%) aligned 0 times
    719904 (97.28%) aligned exactly 1 time
    17028 (2.30%) aligned >1 times
99.58% overall alignment rate

Part 2

Terminal commands: chmod +x map_reads.sh
                            ./map_reads.sh
Output

*** A01_01
740067 reads; of these:
  740067 (100.00%) were unpaired; of these:
    3135 (0.42%) aligned 0 times
    719904 (97.28%) aligned exactly 1 time
    17028 (2.30%) aligned >1 times
99.58% overall alignment rate
*** A01_02
734017 reads; of these:
  734017 (100.00%) were unpaired; of these:
    2795 (0.38%) aligned 0 times
    711921 (96.99%) aligned exactly 1 time
    19301 (2.63%) aligned >1 times
99.62% overall alignment rate
*** A01_03
764931 reads; of these:
  764931 (100.00%) were unpaired; of these:
    3532 (0.46%) aligned 0 times
    742051 (97.01%) aligned exactly 1 time
    19348 (2.53%) aligned >1 times
99.54% overall alignment rate
*** A01_04
792064 reads; of these:
  792064 (100.00%) were unpaired; of these:
    3267 (0.41%) aligned 0 times
    768875 (97.07%) aligned exactly 1 time
    19922 (2.52%) aligned >1 times
99.59% overall alignment rate
*** A01_05
795678 reads; of these:
  795678 (100.00%) were unpaired; of these:
    3038 (0.38%) aligned 0 times
    772606 (97.10%) aligned exactly 1 time
    20034 (2.52%) aligned >1 times
99.62% overall alignment rate
*** A01_06
749541 reads; of these:
  749541 (100.00%) were unpaired; of these:
    3175 (0.42%) aligned 0 times
    725339 (96.77%) aligned exactly 1 time
    21027 (2.81%) aligned >1 times
99.58% overall alignment rate

# Haplotype Visualization

The haplotype visualization in IGV for samples A01_01 through A01_06 (chrI:27,000-32,000) shows coverage and variant positions consistent with the genotype calls in BYxRM_GenoData.txt. Where genotypes differ (BY or RM alleles), read pileups in the BAM files display corresponding nucleotide changes.

Part 4

Terminal commands: minimap2 -ax map-ont sacCer3.fa ERR8562476.fastq > longreads.sam
samtools sort -o longreads.bam longreads.sam
samtools index longreads.bam
samtools idxstats longreads.bam > longreads.idxstats

Output:
[M::mm_idx_gen::0.229*0.99] collected minimizers
[M::mm_idx_gen::0.291*1.41] sorted minimizers
[M::main::0.291*1.41] loaded/built the index for 17 target sequence(s)
[M::mm_mapopt_update::0.311*1.38] mid_occ = 33
[M::mm_idx_stat] kmer size: 15; skip: 10; is_hpc: 0; #seq: 17
[M::mm_idx_stat::0.328*1.36] distinct minimizers: 2084917 (95.68% are singletons); average occurrences: 1.093; average spacing: 5.336; total length: 12157105

Part 5

Terminal commands:

hisat2-build sacCer3.fa sacCer3
hisat2 -p 4 -x sacCer3 -U SRR10143769.fastq -S SRR10143769.sam
samtools sort -o SRR10143769.bam SRR10143769.sam
samtools index SRR10143769.bam

Output:

2917686 reads; of these:
  2917686 (100.00%) were unpaired; of these:
    296807 (10.17%) aligned 0 times
    2245812 (76.97%) aligned exactly 1 time
    375067 (12.85%) aligned >1 times
89.83% overall alignment rate

# RNA-seq gene coverage
In IGV, most coverage is observed in the exonic regions of the active genes; introns are largely spanned due to spliced alignments, making exons show higher read density.