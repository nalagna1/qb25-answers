#!/usr/bin/env bash

wc -l snps-chr1.bed
# 1091148 snps-chr1.bed

awk '$1=="chr1"' hg19-kc.bed > hg19-kc-chr1.bed

bedtools intersect -c -a hg19-kc-chr1.bed -b snps-chr1.bed > gene_snp_counts.chr1.bed

sort -k4,4nr gene_snp_counts.chr1.bed | head -n 1 > top_gene_chr1.txt

cat top_gene_chr1.txt   # chr1  11868  14409  NBPF1  14039

bedtools sample -n 20 -seed 42 snps-chr1.bed > snp20.bed
bedtools sort -i snp20.bed > snp20.sorted.bed
bedtools sort -i hg19-kc.bed > hg19-kc.sorted.bed

bedtools closest -a snp20.sorted.bed -b hg19-kc.sorted.bed -d -t first > snp20.closest.bed

awk '$NF==0' snp20.closest.bed | wc -l   # 7

awk '{print $NF}' snp20.closest.bed | sort -n | (head -n1; tail -n1)
# 0
# 47238

# 7 SNPs lie inside a gene
# distances for outside a gene range from 1 bp to 47,238 bp
# NBPF1 has the most SNPs
# NBPF1 is on chr1:11,868–14,409, size 2,541 bp, 14,039 SNPs
# NBPF1 has the most SNPs likely because it is in a gene family with segmental duplications