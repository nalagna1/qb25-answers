#!/usr/bin/env bash

wget -O hg16.chrom.sizes "https://hgdownload.soe.ucsc.edu/goldenPath/hg16/bigZips/hg16.chrom.sizes"

grep -v _ hg16.chrom.sizes > hg16-main.chrom.sizes
wc -l hg16-main.chrom.sizes   # 24

bedtools makewindows -g hg16-main.chrom.sizes -w 1000000 > hg16-1mb.bed
wc -l hg16-1mb.bed   # 2897

cut -f1-3,5 hg16-kc.tsv > hg16-kc.bed
wc -l hg16-kc.bed   # 74687

bedtools intersect -c -a hg19-1mb.bed -b hg19-kc.bed > hg19-kc-count.bed
bedtools intersect -c -a hg16-1mb.bed -b hg16-kc.bed > hg16-kc-count.bed

bedtools intersect -v -a hg19-kc.bed -b hg16-kc.bed > hg19-only.bed
wc -l hg19-only.bed   # 6590 genes that are only in hg19

bedtools intersect -v -a hg16-kc.bed -b hg19-kc.bed > hg16-only.bed
wc -l hg16-only.bed   # 2007 genes that are only in hg16

wc -l hg19-kc.bed   # genes in hg19 80270
wc -l hg16-kc.bed   # genes in hg16 74687