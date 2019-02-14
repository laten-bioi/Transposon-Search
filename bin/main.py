def main(): #main method
    from BLASTer import makeBlastBD, searchBlastDB
    with open('SoyFileLocation') as db: #need to add actual file path
        makeBlastBD('G.Max',db,'data' ) #need output location

    with open('transposons') as query:
        searchBlastDB() #add parameters



if __name__ == '__main__': #runs main method
    main()
