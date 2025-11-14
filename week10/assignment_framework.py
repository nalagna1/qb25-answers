#!/usr/bin/env python3

import sys

import numpy as np

from fasta import readFASTA


#====================#
# Read in parameters #
#====================#

# The scoring matrix is assumed to be named "sigma_file" and the 
# output filename is assumed to be named "out_file" in later code


# Read the scoring matrix into a dictionary
fs = open(sigma_file)
sigma = {}
alphabet = fs.readline().strip().split()
for line in fs:
	line = line.rstrip().split()
	for i in range(1, len(line)):
		sigma[(alphabet[i - 1], line[0])] = float(line[i])
fs.close()

# Read in the actual sequences using readFASTA


#=====================#
# Initialize F matrix #
#=====================#


#=============================#
# Initialize Traceback Matrix #
#=============================#


#===================#
# Populate Matrices #
#===================#


#========================================#
# Follow traceback to generate alignment #
#========================================#

# The aligned sequences are assumed to be strings named sequence1_aligment
# and sequence2_alignment in later code


#=================================#
# Generate the identity alignment #
#=================================#

# This is just the bit between the two aligned sequences that
# denotes whether the two sequences have perfect identity
# at each position (a | symbol) or not.

identity_alignment = ''
for i in range(len(sequence1_alignment)):
	if sequence1_alignment[i] == sequence2_alignment[i]:
		identity_alignment += '|'
	else:
		identity_alignment += ' '


#===========================#
# Write alignment to output #
#===========================#

# Certainly not necessary, but this writes 100 positions at
# a time to the output, rather than all of it at once.

output = open(out_file, 'w')

for i in range(0, len(identity_alignment), 100):
	output.write(sequence1_alignment[i:i+100] + '\n')
	output.write(identity_alignment[i:i+100] + '\n')
	output.write(sequence2_alignment[i:i+100] + '\n\n\n')


#=============================#
# Calculate sequence identity #
#=============================#


#======================#
# Print alignment info #
#======================#

# You need the number of gaps in each sequence, the sequence identity in
# each sequence, and the total alignment score
