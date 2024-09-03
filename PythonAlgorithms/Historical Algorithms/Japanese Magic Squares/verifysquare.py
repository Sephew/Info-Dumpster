
def verifysquare(square):
    sums = []
    rowsums = [sum(square[i]) for i in range(0,len(square))]
    sums.append(rowsums)
    
    colsums = [sum(row[i] for row in square) for i in range(0,len(square))]
    sums.append(colsums)

    maindiag = sum([square[i][i] for i in range(0,len(square))])
    sums.append([maindiag])

    antidiag = sum([square[i][len(square) - 1 - i] for i in range(0,len(square))])
    sums.append([antidiag])

    flattened = [j for i in sums for j in i ]
    return(len(list(set(flattened))) == 1)

luoshu = [[4,9,2], [3,5,7], [8,1,6]]

print (verifysquare(luoshu))