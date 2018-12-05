class SudokuData:

    #reads sudoku.txt into a 3D boolean matrix
    def __init__(self, fileName : str):
        self.numbers = [[[0 for i in range(9)] for j in range(9)] for k in range(9)] 

        f = open(fileName, 'r')
        linenumber = 0
        for l in f:
            vls = l.split(' ')
            for i in range(len(vls)):
                if not '*' in vls[i]:
                    self.numbers[linenumber][i][int(vls[i].rstrip())-1] = 1
            linenumber += 1
