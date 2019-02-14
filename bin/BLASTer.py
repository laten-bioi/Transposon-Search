import os

def makeBlastBD(title, inputFilePath, out): #Will create local BLASTn database to search elements in
    blastCommand = "makeblastdb -dbtype nucl -in {} -title {} -out {}".format(inputFilePath, title, out)
    os.system(blastCommand)

def searchBlastDB(queryFile, DBname, outputFile): #searches 1 element in the local BLASTn database

     os.system("blastn -query {} -db {} -out {} -outfmt ""10 qseqid qstart qend evalue pident"".format(filePath,DBname,outputFile))
    #Will search for all elements in query file as long as in fasta format
    #Adds the start, end, evalue and p identity

def searchBlastDBSingleSeq(queryFile, DBname, outputFile):
    #Possible method to search a single element from collection at a times
