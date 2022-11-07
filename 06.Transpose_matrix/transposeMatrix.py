def getMatrixValues(rows, cols):
    # Create matrix from user's inputs
    matrix = [
        [int(input(f"colum {j+1} -> ENter {i+1} element:")) for j in range(cols)] for i in range(rows)]

    return matrix

def printMatrix(matrix):
    # Show every row of matrix
    for i in (matrix):
        print(i)

def getTransposeMatrix(matrix):

    transpose = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            transpose[j][i] = matrix[i][j]

    return transpose