library(ggplot2)
library(dplyr)

gt <- read.table("gt_long.txt", header=TRUE)

foo <- filter(gt, sample == "A01_62" & chrom == "chrII")
ggplot(foo, aes(x=as.numeric(pos), y=as.factor(gt), fill=as.factor(gt))) +
  geom_tile() +
  theme_bw() +
  labs(x="Position on chrII", y="Genotype", fill="Ancestry") +
  scale_fill_manual(values=c("blue", "red"))

ggplot(filter(gt, sample == "A01_62"),
       aes(x=as.numeric(pos), y=chrom, fill=as.factor(gt))) +
  geom_tile() +
  facet_grid(chrom ~ ., scales="free_x", space="free_x") +
  theme_bw()

ggplot(gt, aes(x=as.numeric(pos), y=sample, fill=as.factor(gt))) +
  geom_tile() +
  facet_grid(chrom ~ ., scales="free_x", space="free_x") +
  theme_bw()