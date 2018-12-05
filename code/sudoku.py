from sudokudata import SudokuData
from mip.model import *
from sys import stdout as out
from sys import argv

#first program argument must be name of inputfile
inst = SudokuData(argv[1])
numbers = inst.numbers
m=Model()

#define 3D boolean matrix where k defines the value
x = [[[m.add_var(type=BINARY)
        for j in range(9)]
            for i in range(9)]
                 for k in range(9)]

#fixed values constraints
for i in range(9):
    for j in range(9):
        for k in range(9):
            if numbers[i][j][k] == 1:
                m += x[i][j][k] == 1;

#max 1 value per coordinate
for i in range(9):
    for j in range(9):
        m+=xsum(x[i][j][k] for k in range(9)) == 1

#max 1 value of each type per row
for i in range(9):
    for k in range(9):
        m += xsum(x[i][j][k] for j in range(9)) == 1


#max 1 value of each type per column
for j in range(9):
    for k in range(9):
        m += xsum(x[i][j][k] for i in range(9)) == 1
        
#max 1 value of each type per block  
for i2 in range(3):
    for j2 in range(3):
        for k in range(9):
            m += xsum(x[i][j][k]
                for i in range(i2*3,i2*3+3)
                    for j in range(j2*3, j2*3+3)) == 1
                   
m.optimize()

#print solution
for i in range(9):
    for j in range(9):
        for k in range(9):
                if x[i][j][k].x >= 0.99:
                    out.write(str(k+1))
        out.write(' ')
    out.write('\n')


                
