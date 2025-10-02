cross <- read.table("crossovers.txt", sep="\t", header=FALSE, col.names=c("sample","n_cross"))
hist(cross$n_cross, breaks=10, main="Number of Crossovers per Sample", xlab="Number of crossovers")