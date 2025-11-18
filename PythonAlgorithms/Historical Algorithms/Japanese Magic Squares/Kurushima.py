from verifysquare import verifysquare
import math
import random

#set the grid size N x N 
n = 11

#create a NaN matrix
square = [[float('nan') for i in range (0,n)] for j in range(0,n)]


#print(square)
#print it prettier
def printsquare(square):
    labels = ['['+str(x)+']' for x in range(0,len(square))]
    format_row = "{:>6}" * (len(labels) + 1)
    print(format_row.format("",*labels))
    for label, row in zip(labels,square):
        print(format_row.format(label,*row))

#Finds the center of the matrix
center_i = math.floor(n/2)
center_j = math.floor (n/2)

#initialize first 5 squares populated in the expression, based on the rules of Kurushima's Algorithm
square[center_i][center_j] = int((n**2 + 1 )/2)
square[center_i + 1][center_j] = 1
square[center_i - 1][center_j] = n **2
square[center_i][center_j - 1] = n
square[center_i][center_j + 1] = (n**2 + 1) - n


#Rules of Kurushima's Magic Square Algorithm, only applies on ODD N x N matrices
#rule 1 if bottom left to top right or vise versa
#rule 2 if bottome right to top left or vise versa
#rule 3 if crossing anti diag from bottom right to top left or vise versa solely (basically to get the anti diag)

def rule1(x,n, UpperRight):
    return((x + ((-1) ** UpperRight) * n ) % n**2 )
def rule2(x,n, Upperleft):
    return((x + ((-1) ** Upperleft) ) % n**2)
def rule3(x,n, Upperleft):
    return((x + ((-1)** Upperleft * (-n  + 1))) % n**2)


#initialize the entry point as the center
entry_i = center_i
entry_j = center_j


def fillsquare(square,entry_i, entry_j,howfull):
        #checks for the total 'nan' numbers for each row in the square and check if its greater than a threshold, continue if it is.
        while(sum(math.isnan(i) for row in square for i in row) > howfull):
            where_we_can_go = []

            #initializes ways the algorithm can move (diagonal like checkers only)
            if (entry_i < (n -1) and entry_j < (n - 1)):
                where_we_can_go.append('down_right')

            if (entry_i < (n - 1) and entry_j > 0):
                where_we_can_go.append('down_left')

            if (entry_i > 0 and entry_j < (n - 1)):
                where_we_can_go.append('up_right')

            if (entry_i > 0 and entry_j > 0):
                where_we_can_go.append('up_left')
            
            #Randomly Selects the next number to compute for
            where_to_go = random.choice(where_we_can_go)


            if (where_to_go == 'up_right'):
                new_entry_i = entry_i - 1
                new_entry_j = entry_j + 1
                square[new_entry_i][new_entry_j] = rule1(square[entry_i][entry_j],n,True)

            if (where_to_go == 'down_left'):
                new_entry_i = entry_i + 1
                new_entry_j = entry_j - 1
                square[new_entry_i][new_entry_j] = rule1(square[entry_i][entry_j],n,False)

            if (where_to_go == 'up_left'):
                new_entry_i = entry_i - 1
                new_entry_j = entry_j - 1
                square[new_entry_i][new_entry_j] = rule2(square[entry_i][entry_j],n,True)

            if (where_to_go == 'down_right'):
                new_entry_i = entry_i + 1
                new_entry_j = entry_j + 1
                square[new_entry_i][new_entry_j] = rule2(square[entry_i][entry_j],n,False)

            if (where_to_go == 'up_left' and (new_entry_i + new_entry_j) == (n)):
                new_entry_i = entry_i - 1
                new_entry_j = entry_j - 1
                square[new_entry_i][new_entry_j] = rule3(square[entry_i][entry_j],n,True)

            if (where_to_go == 'down_right' and (new_entry_i + new_entry_j) == (n-2)):
                new_entry_i = entry_i + 1
                new_entry_j = entry_j + 1
                square[new_entry_i][new_entry_j] = rule3(square[entry_i][entry_j],n,False)
                
            entry_i = new_entry_i
            entry_j = new_entry_j
        return(square)

#fills the square by half so that it wont waste its time trying to fill in the squares adjacent to it (because it can only move diagonally)
square = fillsquare(square, entry_i,entry_j,(n**2 )/ 2 - 4)

#shift the entry to an adjacent position so it can fill the opposite diagonals
entry_i = math.floor(n/2) + 1
entry_j = math.floor(n/2)
square = fillsquare(square,entry_i,entry_j,0)
#since the algorithm counts from 0 to n**2, we need to make it to 1 to n**2 + 1
square = [[n**2 if x == 0 else x for x in row] for row in square]

#prints the square matrix more elegantly
printsquare(square)

#uses verifysquare.py to verify if its a true magic square
verifysquare(square)
