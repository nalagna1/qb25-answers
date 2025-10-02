cd ~/Data/genomes
cp ~/Data/References/sacCer3/sacCer3.fa.gz .
gunzip sacCer3.fa.gz
bowtie2-build sacCer3.fa sacCer3

cd ~/Data/variants
bowtie2 -p 4 -x ../genomes/sacCer3 -U fastq/A01_01.fq.gz -S A01_01.sam

samtools sort -o A01_01.bam A01_01.sam
samtools index A01_01.bam
samtools idxstats A01_01.bam > A01_01.idxstats

cd week2/rna
fasterq-dump -p SRR10143769
wc -l SRR10143769.fastq    # Should be 11670744

hisat2-build ~/Data/genomes/sacCer3.fa sacCer3

hisat2 -p 4 -x sacCer3 -U SRR10143769.fastq -S rna.sam
samtools sort -o rna.bam rna.sam
samtools index rna.bam

# Coverage is highest at exons, particularly towards the 3' ends of actively transcribed genes. Intronic regions show little/no coverage, consistent with mature mRNA.
