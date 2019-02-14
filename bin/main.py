def main(): #main method
    from BLASTer import makeBlastBD, searchBlastDB
    with open('SoyFileLocation') as db: #need to add actual file path
        makeBlastBD('G.Max',db,'data' ) #need output location

    with open('GMR30_data/GMR30_ids.fasta') as query:
        searchBlastDB('G.Max',query,'GMR30_data/results.txt') 



if __name__ == '__main__': #runs main method
    main()
