# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 00:09:05 2020

@author: Naomi
"""

import re
#Define the input file
INPUT_FILENAME = 'C:/Users/Naomi/Desktop/IBI/Practical/8 Working with strings/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
#Define the output file
OUTPUT_FILENAME = 'C:/Users/Naomi/Desktop/IBI/Practical/IBI1_2019-20/Practical8/mito_gene.fa'
#Find the sequence name
GENE_NAME_RE = re.compile(r'gene:(?P<gene_name>\S+)')
#Define the simple form of the sequence
def print_seq(seq, name, file):
    # Print the name and length
    print(f'>{name} {len(seq)}', file=file)
    # Print the sequences of mitochondria genes
    print(seq, file=file)
#Read the file and output the result in a new fasta file
with open(INPUT_FILENAME) as input_f, open(OUTPUT_FILENAME, 'w') as output_f:
    #Define an empty string to store the sequence name
    name = ''
    #Define an empty string to store the sequence
    seq = ''
    #Loop through the inital file
    for line in input_f:
        #Find the symbol '>'
        if line.startswith('>'):
            if seq:
                print_seq(seq, name, output_f)
            #Find the sequence name
            m = GENE_NAME_RE.search(line)
            name = m.group('gene_name')
            seq = ''
        else:
            #Extract and combine the sequence
            seq = seq + line.strip()
    #Form the simplified sequence
    if seq:
        print_seq(seq, name, output_f)
