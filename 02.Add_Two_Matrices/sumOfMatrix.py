def getMatrixValues(rows, cols):
    # Create matrix from user's inputs
    matrix = [
        [int(input(f"colum {j+1} -> ENter {i+1} element:")) for j in range(cols)] for i in range(rows)]

    return matrix


def sumMatrix (m1, m2):
    # Create resultant matrix
    rows = len(m1)
    cols = len(m1[0])
    sum = [[0 for j in range(cols)] for i in range(rows)]
    
    # Addition
    for i in range(rows):
        for j in range(cols):
            sum[i][j] = m1[i][j] + m2[i][j]
    
    return sum

def printMatrix(matrix):
    # Show every row of matrix
    for i in (matrix):
        print(i)