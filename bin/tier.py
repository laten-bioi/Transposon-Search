import os

#assumes that the Gmax2.0 refernce genome is already good to go on PC

def buildIndex(fastaPath, indexName):
    #will give option to build index from fasta file

    os.system("bowtie2-build {} -f {}").format(fastaPath, indexName)
    os.system("echo index built")
    return indexName


def searchIndex():
    # reads command from the parameters file
    #searches updated index with the consensus seq and returns results to location in .sam

    with open("parameters.txt") as paras:
        #read so that method gets correct para lines
        #read line into command
        search = ""

        os.system(search)
        
