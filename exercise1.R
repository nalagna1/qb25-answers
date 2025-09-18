library(tidyverse)
setwd('/Users/cmdb/qb25-answers/week1')

header <- c( "chr", "start", "end", "count" )

df_kc <- readr::read_tsv("hg19-kc-count.bed", col_names = header)

df_kc %>%
  filter(chr == "chr1") %>%
  ggplot(aes(x = start/1e6, y = count)) +
  geom_line() +
  labs(title = "Gene density on chr1 (1 Mb windows)",
       x = "Position (Mb)",
       y = "Number of knownCanonical transcripts per 1 Mb")

p <- df_kc %>%

  mutate(chr = factor(chr, levels = unique(chr))) %>%
  ggplot(aes(x = start/1e6, y = count)) +
  geom_line() +
  facet_wrap(~ chr, scales = "free_x", ncol = 5) +
  labs(title = "Gene density (hg19) — 1 Mb windows",
       x = "Position (Mb)",
       y = "Genes per 1 Mb")

print(p)

ggsave("exercise1.png", p, width = 12, height = 8, dpi = 300)
