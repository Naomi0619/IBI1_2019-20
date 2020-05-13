# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:23:15 2020

@author: Naomi
"""

import re
INPUT_FILENAME = 'C:/Users/Naomi/Desktop/IBI/Practical/8 Working with strings/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
#Create the nuleotide dictionary
COMPLEMENT = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
##Find the sequence name
GENE_NAME_RE = re.compile(r'gene:(?P<gene_name>\S+)')
#Define the simple form of the sequence
def print_rc_seq(seq, name, file):
    # Print the name and length
    print(f'>{name} {len(seq)}', file=file)
    # Print the sequence
    print(rc_seq(seq), file=file)
#Returns the reverse complementary sequence
def rc_seq(seq):
    complementary_seq = ''.join(COMPLEMENT[c] for c in seq)
    return complementary_seq[::-1]
#Define a function that form more simple sequences
def main():
    output_filename = None
    #Ask the user to input a filename as the new fasta file
    while True:
        output_filename = input(
            'Please enter the filename of the output file: ').strip()
        if output_filename != '':
            break
    #Read the initial file and output the result
    with open(INPUT_FILENAME) as input_f, open(output_filename, 'w') as output_f:
        #Define an empty string to store the sequence name
        name = ''
        #Define an empty string to store the sequence
        seq = ''
         #Loop through the input file
        for line in input_f:
            #Find the symbol '>'
            if line.startswith('>'):
                if seq:
                    print_rc_seq(seq, name, output_f)
                #Find the sequence name
                m = GENE_NAME_RE.search(line)
                name = m.group('gene_name')
                seq = ''
            else:
                #Extract the sequence
                seq = seq + line.strip()
        if seq:
            #Form the simplified sequence
            print_rc_seq(seq, name, output_f)
main()
