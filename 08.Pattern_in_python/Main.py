from patternPython import *

# Print different pattern programs in python such as left triangle pattern, 
# right triangle pattern, diamond shape pattern, pyramid shape pattern, 
# pascals shape pattern, inverted pyramid pattern, hourglass pattern, 
# butterfly pattern, etc. 

def main():
    
    length = int(input("Enter lenght of the pattern: "))

    leftTrianglePattern(length)
    rightTrianglePatter(length)
    pyramidPattern(length)
    invertedPyramidPattern(length)
    diamondPattern(length)
    pascalPattern(length)
    hourglassPattern(length)
    butterflyPattern(length)

    
if __name__ == "__main__":
    main()
