from sumOfMatrix import *

# Add to Matrix2

def main():

# User's inputs:
    rows = int(input("ENter Matrix number of rows: "))
    cols = int(input("ENter Matrix number of colums: "))

# Get values for matrix A 
    print("Enter values for matrix A:")
    matrix_A = getMatrixValues(rows, cols)

# Get values for matrix B 
    print("Enter values for matrix B:")
    matrix_B = getMatrixValues(rows, cols)

# Addition matrix
    result = (sumMatrix(matrix_A, matrix_B))

# Show matrix and addition
    print("Matrix A: ")
    printMatrix(matrix_A)
    print("Matrix B: ")
    printMatrix(matrix_B)
    print("Addition of Matrix-A and Matrix-B is: ")
    printMatrix(result)

if __name__ == "__main__":
    main()
