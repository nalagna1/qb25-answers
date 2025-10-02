af <- read.table("AF.txt", header=TRUE)
hist(af$AF, breaks=11, main="Allele Frequency Spectrum", xlab="Allele Frequency", ylab="Number of Variants")