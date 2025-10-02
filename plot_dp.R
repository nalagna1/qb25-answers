dp <- read.table("DP.txt", header=TRUE)
hist(dp$DP, breaks=21, xlim=c(0,20), main="Distribution of Read Depth", xlab="Read Depth", ylab="Count")