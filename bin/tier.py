import os

#assumes that the Gmax2.0 refernce genome is already good to go on PC

def buildIndex(fastaPath, indexName):
    #will give option to build index from fasta file

    os.system("bowtie2-build {} -f {}").format(fastaPath, indexName)
    os.system("echo index built")
    return indexName


def searchIndex(indexName, SamOutput,):
    #searches updated index with the consensus seq and returns results to location in .sam
    os.system()

    
