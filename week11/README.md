
Step 1.1
GENOME_SIZE = 1_000_000
READ_LENGTH = 100
COVERAGE_X = 3
READS_NEEDED = GENOME_SIZE * COVERAGE_X // READ_LENGTH  # 30,000

Step 1.4
Genome not sequenced (0X coverage) = 0.0064%
Poisson fit: fits quite well except for the left region of the curve.
Normal distribution fit: fits similarly to Poisson but actually slightly
less well.

Step 1.5
Genome not sequenced (0X coverage) = 0.0064%
Poisson fit: fits better than in step 1.4 and better than normal distribution.
Normal distribution fit: fits better than in step 1.4.

Step 1.6
Genome not sequenced (0X coverage) = 0.0001%
Poisson and normal distribution appear to fit quite similarly.

Step 2.4
Command: dot -Tpng debruijn.dot -o ex2_digraph.png

Step 2.5
CTTATTTCA

Step 2.6
Sufficient coverage: Every region must be sequenced multiple times to correct for
sequencing errors and ensure no gaps.

Unique (discriminating) k-mers: Low repeat content and high sequence complexity
help prevent ambiguities in assembly.

High enough k: The value of k in the de Bruijn graph should be large enough to
bridge unique regions but small enough to maintain overlaps.

Error correction: Sequencing errors or missing data can break paths; error
correction further improves assembly.

Consistent and even coverage: To avoid sequencing bias resulting in
unassembled gaps.