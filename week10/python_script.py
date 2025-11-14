import sys
from fasta import readFASTA

# Command-line arguments

fasta_file = sys.argv[1]
matrix_file = sys.argv[2]
gap_penalty = int(sys.argv[3])
output_file = sys.argv[4]

# 1. Read sequences from fasta

sequences = readFASTA(open(fasta_file))
seq1_id, seq1 = sequences[0]
seq2_id, seq2 = sequences[1]

# 2. Read in the scoring matrix from file as a dictionary

with open(matrix_file) as f:
    lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    letters = lines[0].split()
    sigma = {}
    for i, line in enumerate(lines[1:]):
        scores = line.split()
        for j, score in enumerate(scores[1:]):
            sigma[(letters[i], letters[j])] = int(score)

m = len(seq1)
n = len(seq2)

# 3. Initialize F and traceback matrices

F = [[0 for j in range(n+1)] for i in range(m+1)]
traceback = [[None for j in range(n+1)] for i in range(m+1)]

for i in range(1, m+1):
    F[i][0] = F[i-1][0] + gap_penalty
    traceback[i][0] = "up"
for j in range(1, n+1):
    F[0][j] = F[0][j-1] + gap_penalty
    traceback[0][j] = "left"

# 4. Fill in matrices

for i in range(1, m+1):
    for j in range(1, n+1):
        match = F[i-1][j-1] + sigma[(seq1[i-1], seq2[j-1])]
        delete = F[i-1][j] + gap_penalty
        insert = F[i][j-1] + gap_penalty
        maximum = max(match, delete, insert)
        F[i][j] = maximum
        # Tie-breaking: match > delete > insert
        if maximum == match:
            traceback[i][j] = "diag"
        elif maximum == delete:
            traceback[i][j] = "up"
        else:
            traceback[i][j] = "left"

# 5. Traceback to get alignments

alignment1 = []
alignment2 = []
i = m
j = n
while i > 0 or j > 0:
    if i > 0 and j > 0 and traceback[i][j] == "diag":
        alignment1.append(seq1[i-1])
        alignment2.append(seq2[j-1])
        i -= 1
        j -= 1
    elif i > 0 and traceback[i][j] == "up":
        alignment1.append(seq1[i-1])
        alignment2.append("-")
        i -= 1
    elif j > 0 and traceback[i][j] == "left":
        alignment1.append("-")
        alignment2.append(seq2[j-1])
        j -= 1
    else:
        break  # corner case, shouldn't happen

alignment1 = "".join(reversed(alignment1))
alignment2 = "".join(reversed(alignment2))

# 6. Stats

gaps1 = alignment1.count("-")
gaps2 = alignment2.count("-")
matches = sum(a == b and a != "-" and b != "-" for a, b in zip(alignment1, alignment2))
pid1 = 100.0 * matches / max(len(alignment1.replace("-", "")), 1)
pid2 = 100.0 * matches / max(len(alignment2.replace("-", "")), 1)
score = F[m][n]

print("Gaps in sequence 1:", gaps1)
print("Gaps in sequence 2:", gaps2)
print(f"Percent identity (sequence 1): {pid1:.2f}")
print(f"Percent identity (sequence 2): {pid2:.2f}")
print("Alignment score:", score)

# 7. Write alignment file

with open(output_file, "w") as out:
    out.write(f">{seq1_id}_aligned\n{alignment1}\n")
    out.write(f">{seq2_id}_aligned\n{alignment2}\n")