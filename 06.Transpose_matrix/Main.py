from transposeMatrix import *

# Calculate transpose matrix 

def main():

    rows = int(input("Enter the nº of rows: "))
    cols = int(input("Enter the nº of colums: "))
    
    myMatrix = getMatrixValues(rows, cols)
    
    printMatrix(myMatrix)

    printMatrix(getTransposeMatrix(myMatrix))

    
if __name__ == "__main__":
    main()
