# Transposon-Search
This project will update the locations of transposable elements in the updated Williams 82  genome assembly

## The Plan (Probably)

### Step 1
Get a pipeline working that is able to BLAST the elements from the GMR30.txt file (format is FASTA)
The pipeline must be able to read search results for each element and then (I think) take the highest scoring/perfect hit locations and edit the corresponding ID list in the GMR30 IDs file. It will be important data is exported in a way that the start and end of elements is easily extracted, might have to play around with the BLAST search parameters. 

### Step 2
Test pipeline by comparing the result of BLAST search to a few manual online BLAST searched and adjust as needed. Do an other required testing.

### Step 3
Expand dataset to include other transposable elements of interest and follow same procedure.
