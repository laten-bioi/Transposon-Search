import os

#assumes that the Gmax2.0 refernce genome is already good to go on PC

def buildIndex():
    #Builds index from a fasta file, parameters of search given in parameters.txt
    with open('parameters.txt') as paras:
        command = ''
        for line in paras:
            if line == 'INDEX':
                search = paras.nextline()
    os.system(command)
    paras.close()

def searchIndex():
    # reads command from the parameters file
    #searches updated index with the consensus seq and returns results to location in .sam
    with open("parameters.txt") as paras:
         command = ''
         for line in paras:
             if line == 'INDEX':
                 command = paras.nextline()
    os.system(command)
    paras.close()
