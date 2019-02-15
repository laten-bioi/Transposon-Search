# Transposon-Search Background
With the incredible amount of genomic information being produced every day, reference genomes that researchers depend upon for various kinds of genomic studies are updated frequently. This results in many versions of a species genome being publically available at any given time. This can create issues when research done in one version is set to be updated to the newest reference genome, especially for repetitive elements such as retrotransposons. 

This project aims to create an algorithm that will be capable of taking the sequences and locations of repetitive elements from one reference genome version and locating the new positon of that element in the updated version. The algorithm will also catalogue changes to the updated sequence such as insertions or deletions. 


# The Plan (As of 2/15)

## Step 1
The script will first create a consensus sequence from a family of repeated elements using BLAST multiple sequence alignment. The consensus sequence will serve as a best representation of the family in question and limit the impact of outlier elements within the family. 

## Step 2
Use Bowtie to perform a global sequence alignment with the consensus sequence to the reference genome. Hits from the global alignment can then be presumed to be the locations of that repetitive element family within the genome. Ensure that beginnings and ends of sequence are not removed in the allignment.

## Step 3
Analyze output from Bowtie search to give the locations of elements in the family and compare to original sequence lengths to find insertions and/or deletions. Ideally add some visualization to the program using R. 

