#!/usr/bin/env bash

grep "1_Active" nhek.bed > nhek-active.bed
grep "12_Repressed" nhek.bed > nhek-repressed.bed
grep "1_Active" nhlf.bed > nhlf-active.bed
grep "12_Repressed" nhlf.bed > nhlf-repressed.bed

wc -l nhek-active.bed      # 14013
wc -l nhek-repressed.bed   # 32314
wc -l nhlf-active.bed      # 14888
wc -l nhlf-repressed.bed   # 34469

bedtools intersect -u -a nhek-active.bed -b nhlf-active.bed > active-both.bed
wc -l active-both.bed   # 6098

bedtools intersect -v -a nhek-active.bed -b nhlf-active.bed > active-nhek-only.bed
wc -l active-nhek-only.bed   # 7915

bedtools intersect -a nhek-active.bed -b nhlf-active.bed -f 1 > overlap_f1.bed
wc -l overlap_f1.bed   # 4751

bedtools intersect -a nhek-active.bed -b nhlf-active.bed -F 1 > overlap_F1.bed
wc -l overlap_F1.bed   # 3654

bedtools intersect -a nhek-active.bed -b nhlf-active.bed -f 1 -F 1 > overlap_f1F1.bed
wc -l overlap_f1F1.bed   # 2910

bedtools intersect -u -a nhek-active.bed -b nhlf-active.bed > active_active.bed
bedtools intersect -u -a nhek-active.bed -b nhlf-repressed.bed > active_repressed.bed
bedtools intersect -u -a nhek-repressed.bed -b nhlf-repressed.bed > repressed_repressed.bed

wc -l active_active.bed     # 6098 regions active in both NHEK and NHLF
wc -l active_repressed.bed  # 2291 regions active in NHEK but repressed in NHLF
wc -l repressed_repressed.bed # 15234 regions repressed in both